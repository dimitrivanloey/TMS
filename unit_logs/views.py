from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Count, Avg, F, Max, Min, Sum, Q
from django.http import JsonResponse

from datetime import datetime as dt
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

    # jan_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 2, 1, 0, 0, 0))
    # feb_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 3, 1, 0, 0, 0))
    # mar_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 4, 1, 0, 0, 0))
    # apr_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 5, 1, 0, 0, 0))
    # may_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 6, 1, 0, 0, 0))
    # jun_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 7, 1, 0, 0, 0))

    # context = {
    #     'data': {
    #       # 'repair': [jan_data[0], feb_data[0], mar_data[0], apr_data[0], may_data[0], jun_data[0]],
    #       # 'working': [jan_data[1], feb_data[1], mar_data[1], apr_data[1], may_data[1], jun_data[1]],
    #       # 'warning': [jan_data[2], feb_data[2], mar_data[2], apr_data[2], may_data[2], jun_data[2]],
    #       # 'ooa':  [jan_data[3], feb_data[3], mar_data[3], apr_data[3], may_data[3], jun_data[3]],
    #       # 'oos': [jan_data[4], feb_data[4], mar_data[4], apr_data[4], may_data[4], jun_data[4]],
    #       # 'failure': [jan_data[5], feb_data[5], mar_data[5], apr_data[5], may_data[5], jun_data[5]]
    #       'repair': [ may_data[0], jun_data[0]],
    #       'working': [ may_data[1], jun_data[1]],
    #       'warning': [ may_data[2], jun_data[2]],
    #       'ooa':  [ may_data[3], jun_data[3]],
    #       'oos': [ may_data[4], jun_data[4]],
    #       'failure': [may_data[5], jun_data[5]]

    #     }
    # }

    return render(request, 'unit_logs/index.html')


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
            form.save()
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
    # breakpoint()
    context = {
      'trackers_with_status': trackers_with_status,
      'category_lower': category.lower()
    }

    return render(request, 'unit_logs/trackers_with_status.html', context)

def graph_status_per_month(request):
    jan_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 2, 1, 0, 0, 0))
    feb_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 3, 1, 0, 0, 0))
    mar_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 4, 1, 0, 0, 0))
    apr_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 5, 1, 0, 0, 0))
    may_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 6, 1, 0, 0, 0))
    jun_data = Tracker.number_per_category_before_date(datetime.datetime(2021, 7, 1, 0, 0, 0))

    context = {
        'data': {
          # 'repair': [ may_data[0], jun_data[0]],
          # 'working': [ may_data[1], jun_data[1]],
          # 'warning': [ may_data[2], jun_data[2]],
          # 'ooa':  [ may_data[3], jun_data[3]],
          # 'oos': [ may_data[4], jun_data[4]],
          # 'failure': [may_data[5], jun_data[5]]
          'repair': [jan_data[0], feb_data[0], mar_data[0], apr_data[0], may_data[0], jun_data[0]],
          'working': [jan_data[1], feb_data[1], mar_data[1], apr_data[1], may_data[1], jun_data[1]],
          'warning': [jan_data[2], feb_data[2], mar_data[2], apr_data[2], may_data[2], jun_data[2]],
          'ooa':  [jan_data[3], feb_data[3], mar_data[3], apr_data[3], may_data[3], jun_data[3]],
          'oos': [jan_data[4], feb_data[4], mar_data[4], apr_data[4], may_data[4], jun_data[4]],
          'failure': [jan_data[5], feb_data[5], mar_data[5], apr_data[5], may_data[5], jun_data[5]]
        }
    }

    return JsonResponse(context)
