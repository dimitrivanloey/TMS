from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Count, Avg, F, Max, Min, Sum, Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from datetime import timedelta
import datetime
import json
import re
from django.utils import timezone, datastructures

from .models import *
from .forms import *
from unit_logs.models import *



from collections import namedtuple
from django.db import connection
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def status_counts(yyyy, mm):
  mm+=1 ## We are adding a month in order to query all the days of the current month
  if(mm == 12):
    mm = 1
    yyyy += 1

  with connection.cursor() as cursor:
      cursor.execute('select count(tmp2.category), tmp2.category from ( \
        select distinct on(tracker_id) tracker_id, "timestamp", tmp.status_id, unit_logs_status.category from ( \
          select tracker_id, "timestamp", e.status_id from unit_logs_entry as e where "timestamp" < \'' + str(yyyy)+'-'+str(mm)+'-01' + '\' order by 1,"timestamp" desc \
        ) as tmp \
        inner join unit_logs_status on tmp.status_id=unit_logs_status.id \
      ) as tmp2 GROUP BY tmp2.category \
      ')
      results = namedtuplefetchall(cursor)
  return results


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# # Individual Tracker Page
@xframe_options_exempt
@login_required
def tracker_show(request, tracker_group, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    entries = tracker.entry_set.order_by('-timestamp')

    if request.method == 'GET':
        form = TrackerForm(instance=tracker)
        context = {'tracker': tracker, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/tracker_show.html', context)
    else:
        form = TrackerForm(request.POST, instance=tracker)
        form.save()
        return redirect('unit_logs:tracker_show', tracker_group=tracker_group, tracker_id=tracker_id)

# # Main index page
@xframe_options_exempt
@login_required
def index(request):
    tracker_objects = Tracker.objects

    context = {
        'data': {
          'month_titles': month_titles(last_6_months(datetime.datetime.now())),
        }
    }
    return render(request, 'unit_logs/index.html', context)


# # Individual Pages
@xframe_options_exempt
@login_required
def trackers(request, tracker_group):
    trackers = Tracker.objects.filter(tracker_group=tracker_group).order_by('number')
    context = {'trackers' : trackers, 'tracker_group': tracker_group }
    return render(request, 'unit_logs/trackers.html', context)

@xframe_options_exempt
@login_required
def new_tracker(request, tracker_group):
    """Add a new tracker"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TrackerForm()
        form.fields["tracker_group"].initial = str(tracker_group)
    else:
        # POST data submitted; process data
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            tracker = form.save()
            # assign birth event
            tracker.entry_set.create(
              timestamp=datetime.datetime.now(),
              venue=None,
              comments='automatic entry',
              tracker_id=tracker.id,
              status_id=1
            )
            return redirect('unit_logs:trackers', tracker_group=tracker_group)

    # Display a blank or invalid form
    context = {'form': form, 'tracker_group': tracker_group}
    return render(request, 'unit_logs/new_tracker.html', context)

@xframe_options_exempt
@login_required
def delete_tracker(request, tracker_group, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    if request.method == 'POST':
        tracker.delete()
        return redirect('unit_logs:trackers', tracker_group=tracker_group)


@xframe_options_exempt
@login_required
def new_tracker_entry(request, tracker_group, tracker_id):
    """Add a new entry for a particular tracker"""
    tracker = Tracker.objects.get(id=tracker_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm(initial={'tracker': tracker.id})
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_tracker_entry = form.save(commit=False)
            new_tracker_entry.tracker = tracker
            new_tracker_entry.save()
            return redirect('unit_logs:tracker_show', tracker_group=tracker_group, tracker_id=tracker_id)

    # Display a blank or invalid form
    context = {'tracker': tracker, 'form': form, 'tracker_group': tracker_group}
    return render(request, 'unit_logs/new_tracker_entry.html', context)


# # Edit winx entry pages
@xframe_options_exempt
@login_required
def edit_tracker_entry(request, tracker_group, tracker_id, entry_id):
    """Edit an exiting tracker entry"""
    entry = Entry.objects.get(id=entry_id)
    tracker = entry.tracker

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:tracker_show', tracker_group=tracker_group, tracker_id=tracker.id)

    context = {'entry': entry, 'tracker': tracker, 'form': form}
    return render(request, 'unit_logs/edit_tracker_entry.html', context)

@xframe_options_exempt
@login_required
def delete_tracker_entry(request, tracker_group, tracker_id, entry_id):
    entry = Entry.objects.get(id=entry_id)
    tracker = entry.tracker
    if request.method == 'POST':
      entry.delete()
      return redirect('unit_logs:tracker_show', tracker_group=tracker_group, tracker_id=tracker_id)

@xframe_options_exempt
@login_required
def trackers_in_repair(request):
    entries_in_repair = Tracker.latest_entry_in_category('Repair')

    context = {
      'entries_in_repair': entries_in_repair
    }

    return render(request, 'unit_logs/trackers_in_repair.html', context)

@xframe_options_exempt
@login_required
def sticks_missing(request):
    """Show all sticks and missing units from 30 days ago"""
    entries = Entry.objects.filter(date_added__gte=dt.now(tz=timezone.utc)-timedelta(days=30)).filter(Q(status='On Course - Racing: Stuck on track') | Q(status='On Course - Racing: Not to course'))

    context = {'entries':entries}
    return render(request, 'unit_logs/sticks_missing.html', context )


@xframe_options_exempt
@login_required
def tracker_failures(request, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    failures = tracker.failures_set.all().order_by('-start_date')

    context = {'tracker': tracker, 'failures': failures}

    return render(request, 'unit_logs/tracker_failures.html', context)



@xframe_options_exempt
@login_required
def new_tracker_failure(request, tracker_group, tracker_id):
    """Add a new failure entry for a particular tracker"""
    tracker = Tracker.objects.get(id=tracker_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TrackerFailureForm(initial={'tracker': tracker.id, 'start_date': today})
    else:
        # POST data submitted; process data
        form = TrackerFailureForm(data=request.POST)
        if form.is_valid():
            new_tracker_failure = form.save(commit=False)
            new_tracker_failure.tracker = tracker
            new_tracker_failure.save()
            return redirect('unit_logs:tracker_show', tracker_group=tracker_group, tracker_id=tracker_id)

    # Display a blank or invalid form
    context = {'tracker': tracker, 'form': form, 'tracker_group': tracker_group}
    return render(request, 'unit_logs/new_tracker_failure.html', context)

# Edit arkle failure entry pages
@xframe_options_exempt
@login_required
def edit_tracker_failure(request, tracker_group, tracker_id, failure_id):
    """Edit an exiting tracker failure"""
    failure = Failure.objects.get(id=failure_id)
    tracker = failure.tracker

    if request.method != 'POST':
        form = TrackerFailureForm(instance=failure)
    else:
        form = TrackerFailureForm(instance=failure, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:tracker_show', tracker_group=tracker_group, tracker_id=tracker_id)

    context = {'failure': failure, 'tracker': tracker, 'form': form}
    return render(request, 'unit_logs/edit_tracker_failure.html', context)

# Delete tracker failure  pages
@xframe_options_exempt
@login_required
def delete_tracker_failure(request, tracker_group, tracker_id, failure_id):
    failure = Failure.objects.get(id=failure_id)
    tracker = failure.tracker
    if request.method == 'POST':
        failure.delete()
        return redirect('unit_logs:tracker_show', tracker_group=tracker_group, tracker_id=tracker.id)


# Delete tracker failure  pages
@xframe_options_exempt
@login_required
def trackers_with_status(request, category):
    trackers_with_status = [e.tracker for e in Tracker.latest_entry_in_category(category)]

    context = {
      'trackers_with_status': trackers_with_status,
      'category_lower': category.lower()
    }

    return render(request, 'unit_logs/trackers_with_status.html', context)

# last_6_months(datetime.datetime.fromisoformat('2021-12-04'))
# last_6_months(datetime.datetime.fromisoformat('2021-8-04'))
# last_6_months(datetime.datetime.fromisoformat('2021-1-04'))
# This won't work going back more than 12 months..!
def last_6_months(today=datetime.datetime.now()):
  # today = datetime.datetime.now()
  mnth_counter = 0
  dates = []
  year = today.year
  for x in range(0, 6):
    mm = today.month-x
    if(mm > 12):
      mm = 1
      dates.append({'year': year+1, 'month': mm})
    else:
      if(mm <= 0):
        year -= 1
        print(year)
        if(mm == 0):
          mm = 12
        else:
          mm = mm % 12
      dates.append({'year': year, 'month': mm})
  return dates

def month_titles(dates):
  month_map = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6':'Jun', '7':'Jul', '8':'Aug', '9':'Sep', '10':'Oct', '11': 'Nov', '12': 'Dec'}
  return (lambda month_map=month_map,dates=dates: [month_map[str(d['month'])] for d in dates])()[::-1]

def filter(month_data, status):
  l = [t for t in [r if r.category == status else None for r in month_data] if t is not None]
  if(len(l) > 0):
    return l[0].count
  return 0

def graph_status_per_month(request):

    last_months = last_6_months(datetime.datetime.now())
    datas = []

    ordered_entry_sets = [t.entry_set.prefetch_related('status').order_by('timestamp') for t in Tracker.objects.all()]
    all_status_categories = Status.all_categories()

    months = []
    while len(last_months) > 0:
      next_month = last_months.pop()
      months.append(status_counts(next_month['year'], next_month['month']))


    context = {
        'data': {
          'repair': [filter(months[0], 'Repair'), filter(months[1], 'Repair'), filter(months[2], 'Repair'), filter(months[3], 'Repair'), filter(months[4], 'Repair'), filter(months[5], 'Repair')],
          'working': [filter(months[0], 'Working'), filter(months[1], 'Working'), filter(months[2], 'Working'), filter(months[3], 'Working'), filter(months[4], 'Working'), filter(months[5], 'Working')],
          'warning': [filter(months[0], 'Warning'), filter(months[1], 'Warning'), filter(months[2], 'Warning'), filter(months[3], 'Warning'), filter(months[4], 'Warning'), filter(months[5], 'Warning')],
          'ooa':  [filter(months[0], 'OOA'), filter(months[1], 'OOA'), filter(months[2], 'OOA'), filter(months[3], 'OOA'), filter(months[4], 'OOA'), filter(months[5], 'OOA')],
          'oos': [filter(months[0], 'OOS'), filter(months[1], 'OOS'), filter(months[2], 'OOS'), filter(months[3], 'OOS'), filter(months[4], 'OOS'), filter(months[5], 'OOS')],
          'failure': [filter(months[0], 'Failure'), filter(months[1], 'Failure'), filter(months[2], 'Failure'), filter(months[3], 'Failure'), filter(months[4], 'Failure'), filter(months[5], 'Failure')]
        }
    }

    return JsonResponse(context)

@csrf_exempt
def bulk_add_entries(request):
  if request.method == 'POST':
    json.loads(request.body)
    try:
      data = json.loads(request.body)
      for race in data:
        for tracker in race['Trackers']:
          # breakpoint()
          tracker_record = Tracker.objects.get(tracker_group=re.split('(\d+)', tracker['name'])[0], number=re.split('(\d+)', tracker['name'])[1])
          tracker_status_record = Status.objects.get(category=tracker['status'].split(" - ")[0], description=tracker['status'].split(" - ")[1])
          Entry(venue=race['VenueName'], tracker=tracker_record, status=tracker_status_record, comments="automatic ocm").save()
      return JsonResponse({'status': 'ok'}, status=200)
    except:
      return JsonResponse({'status': 'failed'}, status=501)


@csrf_exempt
def entries_for_venue_on_date(request):
  if request.method == 'GET':
    venue_name = request.GET.get('venue_name', False)
    date = request.GET.get('date', False)
    if not venue_name or not date:
      return JsonResponse({'error': 'must pass venue_name and date as params' }, status=400)
    entries = Entry.objects.filter(venue=venue_name, timestamp__contains=date)
    return JsonResponse({'entries': [e.tracker.tracker_group + str(e.tracker.number) for e in entries]}, status=200)
