from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Count, Avg, F, Max, Min, Sum, Q

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
def tracker_show(request, group, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    d0 = dt.now().date()
    if tracker.start_date != None:
        d1 = tracker.start_date
    else:
        d1 = tracker.date_added
    delta = d0 - d1

    entries = tracker.entry_set.order_by('-date_added')
    entries_count = tracker.entry_set.filter(status= 'On Course - Racing: Good Performance').count()
    failures = tracker.failure_set.order_by('-start_date')

    if request.method == 'GET':
        form = TrackerForm(instance=tracker)
        context = {'tracker': tracker, 'form':form, 'entries':entries, 'failures':failures, 'entries_count': entries_count, 'delta': delta}
        return render(request, 'unit_logs/tracker_unit.html', context)
    else:
        form = TrackerForm(request.POST, instance=tracker)
        form.save()
        return redirect('unit_logs:tracker_show', group=group, tracker_id=tracker_id)

# # Main index page
@xframe_options_exempt
@login_required
def index(request):
    tracker_objects = Tracker.objects

    trackers = tracker_objects.order_by('number')
    total_trackers = tracker_objects.count()
    total_trackers_in_service = tracker_objects.filter(status='In Service').count()
    total_trackers_not_in_service = tracker_objects.filter(status='Not In Service').count()
    total_trackers_in_repair = tracker_objects.filter(status='In Repair').count()
    total_trackers_lost = tracker_objects.filter(status='Lost').count()

#     if total_trackers == 0:
#         percentage_total_in_repair = 1
#         percentage_total_in_service = 1
#         percentage_total_not_in_service = 1
#         percentage_total_lost = 1
#     else:
    percentage_in_service = round( total_trackers_in_service/ total_trackers * 100, 2)
    percentage_not_in_service = round( total_trackers_not_in_service/ total_trackers * 100, 2)
    percentage_in_repair = round( total_trackers_in_repair/ total_trackers * 100, 2)
    percentage_lost = round( total_trackers_lost / total_trackers * 100, 2)


#     arkles = Arkle.objects.order_by('number')
#     denmans = Denman.objects.order_by('number')
#     enables = Enable.objects.order_by('number')
#     frankels = Frankel.objects.order_by('number')
#     kautos = Kauto.objects.order_by('number')

    context = {
        'total_trackers': total_trackers,
        'total_trackers_in_service': total_trackers_in_service,
        'total_trackers_not_in_service': total_trackers_not_in_service,
        'total_trackers_in_repair': total_trackers_in_repair,
        'total_trackers_lost': total_trackers_lost,
        'percentage_in_service': percentage_in_service,
        'percentage_not_in_service': percentage_not_in_service,
        'percentage_in_repair': percentage_in_repair,
        'percentage_lost': percentage_lost
#         'winxes' : winxes,
#         'arkles' : arkles,
#         'denmans' : denmans,
#         'enables' : enables,
#         'frankels' : frankels,
#         'kautos' : kautos,
#         'winxes_total': winxes_total,
#         'winxes_in_service': winxes_in_service,
#         'winxes_not_in_service': winxes_not_in_service,
#         'winxes_in_repair': winxes_in_repair,
#         'enables_total': enables_total,
#         'enables_in_service': enables_in_service,
#         'enables_not_in_service': enables_not_in_service,
#         'enables_in_repair': enables_in_repair,
#         'arkles_total': arkles_total,
#         'arkles_in_service': arkles_in_service,
#         'arkles_not_in_service': arkles_not_in_service,
#         'arkles_in_repair': arkles_in_repair,
#         'denmans_total': denmans_total,
#         'denmans_in_service': denmans_in_service,
#         'denmans_not_in_service': denmans_not_in_service,
#         'denmans_in_repair': denmans_in_repair,
#         'kautos_total': kautos_total,
#         'kautos_in_service': kautos_in_service,
#         'kautos_not_in_service': kautos_not_in_service,
#         'kautos_in_repair': kautos_in_repair,
#         'frankels_total': frankels_total,
#         'frankels_in_service': frankels_in_service,
#         'frankels_not_in_service': frankels_not_in_service,
#         'frankels_in_repair': frankels_in_repair,
#         'others_total': others_total,
#         'others_in_service': others_in_service,
#         'others_not_in_service': others_not_in_service,
#         'others_in_repair': others_in_repair,
#         'winxes_lost': winxes_lost,
#         'arkles_lost': arkles_lost,
#         'denmans_lost': denmans_lost,
#         'enables_lost': enables_lost,
#         'frankels_lost': frankels_lost,
#         'kautos_lost': kautos_lost,
#         'others_lost': others_lost,


    }
    return render(request, 'unit_logs/index.html', context)



# # Individual Pages
@xframe_options_exempt
@login_required
def trackers(request, group):
    trackers = Tracker.objects.filter(group=group).order_by('number')
    context = {'trackers' : trackers, 'group': group }
    return render(request, 'unit_logs/trackers.html', context)

@xframe_options_exempt
@login_required
def new_tracker(request, group):
    """Add a new tracker"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TrackerForm()
        form.fields["group"].initial = str(group)
    else:
        # POST data submitted; process data
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:trackers', group=group)

    # Display a blank or invalid form
    context = {'form': form, 'group': group}
    return render(request, 'unit_logs/new_tracker.html', context)

@xframe_options_exempt
@login_required
def delete_tracker(request, group, tracker_id):
    tracker = Tracker.objects.get(id=tracker_id)
    if request.method == 'POST':
        tracker.delete()
        return redirect('unit_logs:trackers', group=group)


@xframe_options_exempt
@login_required
def new_tracker_entry(request, group, tracker_id):
    """Add a new entry for a particular tracker"""
    tracker = Tracker.objects.get(id=tracker_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_tracker_entry = form.save(commit=False)
            new_tracker_entry.tracker = tracker
            new_tracker_entry.save()
            return redirect('unit_logs:tracker_show', group=group, tracker_id=tracker_id)

    # Display a blank or invalid form
    context = {'tracker': tracker, 'form': form, 'group': group}
    return render(request, 'unit_logs/new_tracker_entry.html', context)


# # Edit winx entry pages
@xframe_options_exempt
@login_required
def edit_tracker_entry(request, group, tracker_id, entry_id):
    """Edit an exiting tracker entry"""
    entry = Entry.objects.get(id=entry_id)
    tracker = entry.tracker

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            # TODO: something wrong with this...!
            return redirect('unit_logs:tracker_show', group=group, tracker_id=tracker.id)

    context = {'entry': entry, 'tracker': tracker, 'form': form}
    return render(request, 'unit_logs/edit_tracker_entry.html', context)

@xframe_options_exempt
@login_required
def delete_tracker_entry(request, group, tracker_id, entry_id):
    entry = Entry.objects.get(id=entry_id)
    tracker = entry.tracker
    if request.method == 'POST':
      entry.delete()
      return redirect('unit_logs:tracker_show', group=group, tracker_id=tracker_id)

@xframe_options_exempt
@login_required
def trackers_in_repair(request):
    trackers_in_repair = Tracker.objects.filter(status='In Repair')

    context = {
      'trackers_in_repair': trackers_in_repair
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
def new_tracker_failure(request, group, tracker_id):
    """Add a new failure entry for a particular tracker"""
    tracker = Tracker.objects.get(id=tracker_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TrackerFailureForm(initial={'tracker': tracker.id, 'start_date': today})
        # form.fields["tracker"].initial = str(tracker)
    else:
        # POST data submitted; process data
        form = TrackerFailureForm(data=request.POST)
        if form.is_valid():
            new_tracker_failure = form.save(commit=False)
            new_tracker_failure.tracker = tracker
            new_tracker_failure.save()
            return redirect('unit_logs:tracker_show', group=group, tracker_id=tracker_id)

    # Display a blank or invalid form
    context = {'tracker': tracker, 'form': form, 'group': group}
    return render(request, 'unit_logs/new_tracker_failure.html', context)

# Edit arkle failure entry pages
@xframe_options_exempt
@login_required
def edit_tracker_failure(request, group, tracker_id, failure_id):
    """Edit an exiting tracker failure"""
    failure = Failure.objects.get(id=failure_id)
    tracker = failure.tracker

    if request.method != 'POST':
        form = TrackerFailureForm(instance=failure)
    else:
        form = TrackerFailureForm(instance=failure, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:tracker_show', group=group, tracker_id=tracker_id)

    context = {'failure': failure, 'tracker': tracker, 'form': form}
    return render(request, 'unit_logs/edit_tracker_failure.html', context)

# Delete tracker failure  pages
@xframe_options_exempt
@login_required
def delete_tracker_failure(request, group, tracker_id, failure_id):
    failure = Failure.objects.get(id=failure_id)
    tracker = failure.tracker
    if request.method == 'POST':
        failure.delete()
        return redirect('unit_logs:tracker_show', group=group, tracker_id=tracker.id)
