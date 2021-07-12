from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Count, Avg, F, Max, Min, Sum, Q
from django.http import JsonResponse

from datetime import datetime
from datetime import timedelta
import datetime
from django.utils import timezone

from .models import *
from .forms import *
from unit_logs.models import *


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
def last_6_months(today):
  # today = datetime.datetime.now()
  mnth_counter = 0
  dates = []
  for x in range(-1, 6-1):
    if today.month == 12 and x <0:
      dates.append({'year': today.year + 1, 'month': 1})
    elif  today.month - x > 0: # normal op - something like jun - 1 = july # its december, so we want all before jan 1st next year
      dates.append({'year': today.year, 'month': today.month-x})
    elif today.month - x <= 0: # its january
      dates.append({'year': today.year - 1, 'month': (today.month - x)+12})
    else: # not sure
      raise Exception
  return dates

def month_titles(dates):
  month_map = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6':'Jun', '7':'Jul', '8':'Aug', '9':'Sep', '10':'Oct', '11': 'Nov', '12': 'Dec'}
  return (lambda month_map=month_map,dates=dates: [month_map[str(d['month']-1)] for d in dates])()[::-1]

def graph_status_per_month(request):

    last_months = last_6_months(datetime.datetime.now())
    datas = []

    while len(last_months) > 0:
      next_month = last_months.pop()
      datas.append(Tracker.number_per_category_before_date(datetime.datetime(next_month['year'], next_month['month'], 1, 0,0,0)))

    month_1 = datas[0]
    month_2 = datas[1]
    month_3 = datas[2]
    month_4 = datas[3]
    month_5 = datas[4]
    month_6 = datas[5]

    context = {
        'data': {
          'repair': [month_1[0], month_2[0], month_3[0], month_4[0], month_5[0], month_6[0]],
          'working': [month_1[1], month_2[1], month_3[1], month_4[1], month_5[1], month_6[1]],
          'warning': [month_1[2], month_2[2], month_3[2], month_4[2], month_5[2], month_6[2]],
          'ooa':  [month_1[3], month_2[3], month_3[3], month_4[3], month_5[3], month_6[3]],
          'oos': [month_1[4], month_2[4], month_3[4], month_4[4], month_5[4], month_6[4]],
          'failure': [month_1[5], month_2[5], month_3[5], month_4[5], month_5[5], month_6[5]]
        }
    }

    return JsonResponse(context)
