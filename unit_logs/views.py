from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models import Count

from datetime import datetime as dt
import datetime

from .models import Winx, Arkle, Denman, Enable, Frankel, Kauto, Entry, Other
from .forms import WinxForm, ArkleForm, DenmanForm, EnableForm, FrankelForm, KautoForm, OtherForm, EntryForm, EnableEntryForm, ArkleEntryForm, DenmanEntryForm, KautoEntryForm, FrankelEntryForm
from unit_logs.models import Arkle_Entry, Denman_Entry, Enable_Entry, Frankel_Entry, Kauto_Entry, Other_Entry
from unit_logs.forms import OtherEntryForm


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)


# Individual OCM Pages
@xframe_options_exempt
def winx_page(request):
    winxes_missing = Winx.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    winxes_stick = Winx.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'winxes_missing' : winxes_missing, 'winxes_stick': winxes_stick}
    return render(request, 'unit_logs/winx.html', context)

@xframe_options_exempt
def arkle_page(request):
    arkles_missing = Arkle.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    arkles_stick = Arkle.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'arkles_missing' : arkles_missing, 'arkles_stick': arkles_stick}
    return render(request, 'unit_logs/arkle.html', context)

@xframe_options_exempt
def denman_page(request):
    denmans_missing = Denman.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    denmans_stick = Denman.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'denmans_missing' : denmans_missing, 'denmans_stick': denmans_stick}
    return render(request, 'unit_logs/denman.html', context)

@xframe_options_exempt
def enable_page(request):
    enables_missing = Enable.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    enables_stick = Enable.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'enables_missing' : enables_missing, 'enables_stick': enables_stick}
    return render(request, 'unit_logs/enable.html', context)

@xframe_options_exempt
def frankel_page(request):
    frankels_missing = Frankel.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    frankels_stick = Frankel.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'frankels_missing' : frankels_missing, 'frankels_stick': frankels_stick}
    return render(request, 'unit_logs/frankel.html', context)

@xframe_options_exempt
def kauto_page(request):
    kautos_missing = Kauto.objects.filter(date_added = today, status = 'MISSING').order_by('-date_added', 'number')
    kautos_stick = Kauto.objects.filter(date_added = today, status = 'STICK').order_by('-date_added', 'number')
    context = {'kautos_missing' : kautos_missing, 'kautos_stick': kautos_stick}
    return render(request, 'unit_logs/kauto.html', context)



# Main index page
@xframe_options_exempt
@login_required
def index(request):
    winxes = Winx.objects.order_by('number')
    winxes_total = Winx.objects.count()
    winxes_in_service = Winx.objects.filter(status='IN SERVICE').count()
    winxes_not_in_service = Winx.objects.filter(status='NOT IN SERVICE').count()
    winxes_in_repair = Winx.objects.filter(status='IN REPAIR').count()

    enables_total = Enable.objects.count()
    enables_in_service = Enable.objects.filter(status='IN SERVICE').count()
    enables_not_in_service = Enable.objects.filter(status='NOT IN SERVICE').count()
    enables_in_repair = Enable.objects.filter(status='IN REPAIR').count()

    arkles_total = Arkle.objects.count()
    arkles_in_service = Arkle.objects.filter(status='IN SERVICE').count()
    arkles_not_in_service = Arkle.objects.filter(status='NOT IN SERVICE').count()
    arkles_in_repair = Arkle.objects.filter(status='IN REPAIR').count()

    denmans_total = Denman.objects.count()
    denmans_in_service = Denman.objects.filter(status='IN SERVICE').count()
    denmans_not_in_service = Denman.objects.filter(status='NOT IN SERVICE').count()
    denmans_in_repair = Denman.objects.filter(status='IN REPAIR').count()

    kautos_total = Kauto.objects.count()
    kautos_in_service = Kauto.objects.filter(status='IN SERVICE').count()
    kautos_not_in_service = Kauto.objects.filter(status='NOT IN SERVICE').count()
    kautos_in_repair = Kauto.objects.filter(status='IN REPAIR').count()

    frankels_total = Frankel.objects.count()
    frankels_in_service = Frankel.objects.filter(status='IN SERVICE').count()
    frankels_not_in_service = Frankel.objects.filter(status='NOT IN SERVICE').count()
    frankels_in_repair = Frankel.objects.filter(status='IN REPAIR').count()

    others_total = Other.objects.count()
    others_in_service = Other.objects.filter(status='IN SERVICE').count()
    others_not_in_service = Other.objects.filter(status='NOT IN SERVICE').count()
    others_in_repair = Other.objects.filter(status='IN REPAIR').count()

    total_trackers = winxes_total + enables_total + arkles_total + denmans_total + kautos_total + frankels_total + others_total
    total_in_service = winxes_in_service + enables_in_service + arkles_in_service + denmans_in_service + kautos_in_service + frankels_in_service + others_in_service
    total_not_in_service = winxes_not_in_service + enables_not_in_service + arkles_not_in_service + denmans_not_in_service + kautos_not_in_service + frankels_not_in_service + others_not_in_service
    total_in_repair = winxes_in_repair + enables_in_repair + arkles_in_repair + denmans_in_repair + kautos_in_repair + frankels_in_repair + others_in_repair

    percentage_total_in_service = round( total_in_service/ total_trackers * 100, 2)
    percentage_total_not_in_service = round( total_not_in_service/ total_trackers * 100, 2)
    percentage_total_in_repair = round( total_in_repair/ total_trackers * 100, 2)


    arkles = Arkle.objects.order_by('number')
    denmans = Denman.objects.order_by('number')
    enables = Enable.objects.order_by('number')
    frankels = Frankel.objects.order_by('number')
    kautos = Kauto.objects.order_by('number')

    context = {
        'total_trackers': total_trackers,
        'total_in_service': total_in_service,
        'total_not_in_service': total_not_in_service,
        'total_in_repair': total_in_repair,
        'percentage_total_in_service': percentage_total_in_service,
        'percentage_total_not_in_service': percentage_total_not_in_service,
        'percentage_total_in_repair': percentage_total_in_repair,
        'winxes' : winxes, 
        'arkles' : arkles, 
        'denmans' : denmans, 
        'enables' : enables, 
        'frankels' : frankels, 
        'kautos' : kautos, 
        'winxes_total': winxes_total, 
        'winxes_in_service': winxes_in_service,
        'winxes_not_in_service': winxes_not_in_service,
        'winxes_in_repair': winxes_in_repair,
        'enables_total': enables_total, 
        'enables_in_service': enables_in_service,
        'enables_not_in_service': enables_not_in_service,
        'enables_in_repair': enables_in_repair,
        'arkles_total': arkles_total, 
        'arkles_in_service': arkles_in_service,
        'arkles_not_in_service': arkles_not_in_service,
        'arkles_in_repair': arkles_in_repair,
        'denmans_total': denmans_total, 
        'denmans_in_service': denmans_in_service,
        'denmans_not_in_service': denmans_not_in_service,
        'denmans_in_repair': denmans_in_repair,
        'kautos_total': kautos_total, 
        'kautos_in_service': kautos_in_service,
        'kautos_not_in_service': kautos_not_in_service,
        'kautos_in_repair': kautos_in_repair,
        'frankels_total': frankels_total, 
        'frankels_in_service': frankels_in_service,
        'frankels_not_in_service': frankels_not_in_service,
        'frankels_in_repair': frankels_in_repair,
        'others_total': others_total, 
        'others_in_service': others_in_service,
        'others_not_in_service': others_not_in_service,
        'others_in_repair': others_in_repair


    }
    return render(request, 'unit_logs/index.html', context)



# Individual Pages
@xframe_options_exempt
@login_required
def winxes(request):
    winxes = Winx.objects.order_by('number')
    context = {'winxes' : winxes}
    return render(request, 'unit_logs/winxes.html', context)

@xframe_options_exempt
@login_required
def winx(request, winx_id):
    winx = Winx.objects.get(id=winx_id)
    entries = winx.entry_set.order_by('-date_added')
    entries_count = winx.entry_set.filter(status= 'Good Performance').count()
    
    if request.method == 'GET':
        form = WinxForm(instance=winx)
        context = {'winx': winx, 'form':form, 'entries':entries, 'entries_count': entries_count}
        return render(request, 'unit_logs/winx_unit.html', context)
    else:
        form = WinxForm(request.POST, instance=winx)
        form.save()
        return redirect('unit_logs:winxes')
    
@xframe_options_exempt
@login_required
def enable(request, enable_id):
    enable = Enable.objects.get(id=enable_id)
    entries = enable.enable_entry_set.order_by('-date_added')

    if request.method == 'GET':
        form = EnableForm(instance=enable)
        context = {'enable': enable, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/enable_unit.html', context)
    else:
        form = EnableForm(request.POST, instance=enable)
        form.save()
        return redirect('unit_logs:enables')

@xframe_options_exempt
@login_required
def arkle(request, arkle_id):
    arkle = Arkle.objects.get(id=arkle_id)
    entries = arkle.arkle_entry_set.order_by('-date_added')

    if request.method == 'GET':
        form = ArkleForm(instance=arkle)
        context = {'arkle': arkle, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/arkle_unit.html', context)
    else:
        form = ArkleForm(request.POST, instance=arkle)
        form.save()
        return redirect('unit_logs:arkles')
        
@xframe_options_exempt
@login_required
def denman(request, denman_id):
    denman = Denman.objects.get(id=denman_id)
    entries = denman.denman_entry_set.order_by('-date_added')

    if request.method == 'GET':
        form = DenmanForm(instance=denman)
        context = {'denman': denman, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/denman_unit.html', context)
    else:
        form = DenmanForm(request.POST, instance=denman)
        form.save()
        return redirect('unit_logs:denmans')

@xframe_options_exempt
@login_required
def kauto(request, kauto_id):
    kauto = Kauto.objects.get(id=kauto_id)
    entries = kauto.kauto_entry_set.order_by('-date_added')

    if request.method == 'GET':
        form = KautoForm(instance=kauto)
        context = {'kauto': kauto, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/kauto_unit.html', context)
    else:
        form = KautoForm(request.POST, instance=kauto)
        form.save()
        return redirect('unit_logs:kautos')


@xframe_options_exempt
@login_required
def frankel(request, frankel_id):
    frankel = Frankel.objects.get(id=frankel_id)
    entries = frankel.frankel_entry_set.order_by('-date_added')

    if request.method == 'GET':
        form = FrankelForm(instance=frankel)
        context = {'frankel': frankel, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/frankel_unit.html', context)
    else:
        form = FrankelForm(request.POST, instance=frankel)
        form.save()
        return redirect('unit_logs:frankels')

@xframe_options_exempt
@login_required
def other(request, other_id):
    other = Other.objects.get(id=other_id)
    entries = other.other_entry_set.order_by('-date_added')

    if request.method == 'GET':
        form = OtherForm(instance=other)
        context = {'other': other, 'form':form, 'entries':entries}
        return render(request, 'unit_logs/other_unit.html', context)
    else:
        form = OtherForm(request.POST, instance=other)
        form.save()
        return redirect('unit_logs:others')

@xframe_options_exempt
@login_required
def arkles(request):
    arkles = Arkle.objects.order_by('number')
    context = {'arkles' : arkles}
    return render(request, 'unit_logs/arkles.html', context)



@xframe_options_exempt
@login_required
def denmans(request):
    denmans = Denman.objects.order_by('number')
    context = {'denmans' : denmans}
    return render(request, 'unit_logs/denmans.html', context)


@xframe_options_exempt
@login_required
def enables(request):
    enables = Enable.objects.order_by('number')
    context = {'enables' : enables}
    return render(request, 'unit_logs/enables.html', context)


@xframe_options_exempt
@login_required
def frankels(request):
    frankels = Frankel.objects.order_by('number')
    context = {'frankels' : frankels}
    return render(request, 'unit_logs/frankels.html', context)



@xframe_options_exempt
@login_required
def kautos(request):
    kautos = Kauto.objects.order_by('number')
    context = {'kautos' : kautos}
    return render(request, 'unit_logs/kautos.html', context)


@xframe_options_exempt
@login_required
def others(request):
    others = Other.objects.order_by('number')
    context = {'others' : others}
    return render(request, 'unit_logs/others.html', context)


@xframe_options_exempt
@login_required
def new_winx(request):
    """Add a new winx"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = WinxForm()
    else:
        # POST data submitted; process data
        form = WinxForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:winxes')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_winx.html', context)


@xframe_options_exempt
@login_required
def new_arkle(request):
    """Add a new arkle"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ArkleForm()
    else:
        # POST data submitted; process data
        form = ArkleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:arkles')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_arkle.html', context)


@xframe_options_exempt
@login_required
def new_denman(request):
    """Add a new denman"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = DenmanForm()
    else:
        # POST data submitted; process data
        form = DenmanForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:denmans')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_denman.html', context)


@xframe_options_exempt
@login_required
def new_enable(request):
    """Add a new enable"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EnableForm()
    else:
        # POST data submitted; process data
        form = EnableForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:enables')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_enable.html', context)


@xframe_options_exempt
@login_required
def new_frankel(request):
    """Add a new frankel"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = FrankelForm()
    else:
        # POST data submitted; process data
        form = FrankelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:frankels')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_frankel.html', context)


@xframe_options_exempt
@login_required
def new_kauto(request):
    """Add a new kauto"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = KautoForm()
    else:
        # POST data submitted; process data
        form = KautoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:kautos')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_kauto.html', context)

@xframe_options_exempt
@login_required
def new_other(request):
    """Add a new other"""
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = OtherForm()
    else:
        # POST data submitted; process data
        form = OtherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:others')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'unit_logs/new_other.html', context)


@xframe_options_exempt
@login_required
def deletewinx(request, winx_id):
    winx = Winx.objects.get(id=winx_id)
    if request.method == 'POST':
        winx.delete()
        return redirect('unit_logs:winxes')


@xframe_options_exempt
@login_required
def deletearkle(request, arkle_id):
    arkle = Arkle.objects.get(id=arkle_id)
    if request.method == 'POST':
        arkle.delete()
        return redirect('unit_logs:arkles')


@xframe_options_exempt
@login_required
def deletedenman(request, denman_id):
    denman = Denman.objects.get(id=denman_id)
    if request.method == 'POST':
        denman.delete()
        return redirect('unit_logs:denmans')


@xframe_options_exempt
@login_required
def deleteenable(request, enable_id):
    enable = Enable.objects.get(id=enable_id)
    if request.method == 'POST':
        enable.delete()
        return redirect('unit_logs:enables')


@xframe_options_exempt
@login_required
def deletefrankel(request, frankel_id):
    frankel = Frankel.objects.get(id=frankel_id)
    if request.method == 'POST':
        frankel.delete()
        return redirect('unit_logs:frankels')


@xframe_options_exempt
@login_required
def deletekauto(request, kauto_id):
    kauto = Kauto.objects.get(id=kauto_id)
    if request.method == 'POST':
        kauto.delete()
        return redirect('unit_logs:kautos')

@xframe_options_exempt
@login_required
def deleteother(request, other_id):
    other = Other.objects.get(id=other_id)
    if request.method == 'POST':
        other.delete()
        return redirect('unit_logs:others')


@xframe_options_exempt
@login_required
def new_winx_entry(request, winx_id):
    """Add a new entry for a particular winx"""
    winx = Winx.objects.get(id=winx_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_winx_entry = form.save(commit=False)
            new_winx_entry.winx = winx
            new_winx_entry.save()
            return redirect('unit_logs:winx', winx_id=winx_id)

    # Display a blank or invalid form
    context = {'winx': winx, 'form': form}
    return render(request, 'unit_logs/new_winx_entry.html', context)

@xframe_options_exempt
@login_required
def new_enable_entry(request, enable_id):
    """Add a new entry for a particular enable"""
    enable = Enable.objects.get(id=enable_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EnableEntryForm(data=request.POST)
        if form.is_valid():
            new_enable_entry = form.save(commit=False)
            new_enable_entry.enable = enable
            new_enable_entry.save()
            return redirect('unit_logs:enable', enable_id=enable_id)

    # Display a blank or invalid form
    context = {'enable': enable, 'form': form}
    return render(request, 'unit_logs/new_enable_entry.html', context)

@xframe_options_exempt
@login_required
def new_arkle_entry(request, arkle_id):
    """Add a new entry for a particular arkle"""
    arkle = Arkle.objects.get(id=arkle_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = ArkleEntryForm()
    else:
        # POST data submitted; process data
        form = ArkleEntryForm(data=request.POST)
        if form.is_valid():
            new_arkle_entry = form.save(commit=False)
            new_arkle_entry.arkle = arkle
            new_arkle_entry.save()
            return redirect('unit_logs:arkle', arkle_id=arkle_id)

    # Display a blank or invalid form
    context = {'arkle': arkle, 'form': form}
    return render(request, 'unit_logs/new_arkle_entry.html', context)


@xframe_options_exempt
@login_required
def new_denman_entry(request, denman_id):
    """Add a new entry for a particular denman"""
    denman = Denman.objects.get(id=denman_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = DenmanEntryForm()
    else:
        # POST data submitted; process data
        form = DenmanEntryForm(data=request.POST)
        if form.is_valid():
            new_denman_entry = form.save(commit=False)
            new_denman_entry.denman = denman
            new_denman_entry.save()
            return redirect('unit_logs:denman', denman_id=denman_id)

    # Display a blank or invalid form
    context = {'denman': denman, 'form': form}
    return render(request, 'unit_logs/new_denman_entry.html', context)

@xframe_options_exempt
@login_required
def new_kauto_entry(request, kauto_id):
    """Add a new entry for a particular kauto"""
    kauto = Kauto.objects.get(id=kauto_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = KautoEntryForm()
    else:
        # POST data submitted; process data
        form = KautoEntryForm(data=request.POST)
        if form.is_valid():
            new_kauto_entry = form.save(commit=False)
            new_kauto_entry.kauto = kauto
            new_kauto_entry.save()
            return redirect('unit_logs:kauto', kauto_id=kauto_id)

    # Display a blank or invalid form
    context = {'kauto': kauto, 'form': form}
    return render(request, 'unit_logs/new_kauto_entry.html', context)

@xframe_options_exempt
@login_required
def new_frankel_entry(request, frankel_id):
    """Add a new entry for a particular frankel"""
    frankel = Frankel.objects.get(id=frankel_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = FrankelEntryForm()
    else:
        # POST data submitted; process data
        form = FrankelEntryForm(data=request.POST)
        if form.is_valid():
            new_frankel_entry = form.save(commit=False)
            new_frankel_entry.frankel = frankel
            new_frankel_entry.save()
            return redirect('unit_logs:frankel', frankel_id=frankel_id)

    # Display a blank or invalid form
    context = {'frankel': frankel, 'form': form}
    return render(request, 'unit_logs/new_frankel_entry.html', context)

@xframe_options_exempt
@login_required
def new_other_entry(request, other_id):
    """Add a new entry for a particular other"""
    other = Other.objects.get(id=other_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = OtherEntryForm()
    else:
        # POST data submitted; process data
        form = OtherEntryForm(data=request.POST)
        if form.is_valid():
            new_other_entry = form.save(commit=False)
            new_other_entry.other = other
            new_other_entry.save()
            return redirect('unit_logs:other', other_id=other_id)

    # Display a blank or invalid form
    context = {'other': other, 'form': form}
    return render(request, 'unit_logs/new_other_entry.html', context)


# Edit winx entry pages
@xframe_options_exempt
@login_required
def edit_winx_entry(request, entry_id):
    """Edit an exiting winx entry"""
    entry = Entry.objects.get(id=entry_id)
    winx = entry.winx

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:winx', winx_id=winx.id)

    context = {'entry': entry, 'winx': winx, 'form': form}
    return render(request, 'unit_logs/edit_winx_entry.html', context)

@xframe_options_exempt
@login_required
def delete_winx_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    winx = entry.winx
    if request.method == 'POST':
        entry.delete()
        return redirect('unit_logs:winx', winx_id=winx.id)


# Edit enable entry pages
@xframe_options_exempt
@login_required
def edit_enable_entry(request, entry_id):
    """Edit an exiting enable entry"""
    entry = Enable_Entry.objects.get(id=entry_id)
    enable = entry.enable

    if request.method != 'POST':
        form = EnableEntryForm(instance=entry)
    else:
        form = EnableEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:enable', enable_id=enable.id)

    context = {'entry': entry, 'enable': enable, 'form': form}
    return render(request, 'unit_logs/edit_enable_entry.html', context)

@xframe_options_exempt
@login_required
def delete_enable_entry(request, entry_id):
    entry = Enable_Entry.objects.get(id=entry_id)
    enable = entry.enable
    if request.method == 'POST':
        entry.delete()
        return redirect('unit_logs:enable', enable_id=enable.id)

# Edit arkle entry pages
@xframe_options_exempt
@login_required
def edit_arkle_entry(request, entry_id):
    """Edit an exiting arkle entry"""
    entry = Arkle_Entry.objects.get(id=entry_id)
    arkle = entry.arkle

    if request.method != 'POST':
        form = ArkleEntryForm(instance=entry)
    else:
        form = ArkleEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:arkle', arkle_id=arkle.id)

    context = {'entry': entry, 'arkle': arkle, 'form': form}
    return render(request, 'unit_logs/edit_arkle_entry.html', context)

@xframe_options_exempt
@login_required
def delete_arkle_entry(request, entry_id):
    entry = Arkle_Entry.objects.get(id=entry_id)
    arkle = entry.arkle
    if request.method == 'POST':
        entry.delete()
        return redirect('unit_logs:arkle', arkle_id=arkle.id)

# Edit denman entry pages
@xframe_options_exempt
@login_required
def edit_denman_entry(request, entry_id):
    """Edit an exiting denman entry"""
    entry = Denman_Entry.objects.get(id=entry_id)
    denman = entry.denman

    if request.method != 'POST':
        form = DenmanEntryForm(instance=entry)
    else:
        form = DenmanEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:denman', denman_id=denman.id)

    context = {'entry': entry, 'denman': denman, 'form': form}
    return render(request, 'unit_logs/edit_denman_entry.html', context)


@xframe_options_exempt
@login_required
def delete_denman_entry(request, entry_id):
    entry = Denman_Entry.objects.get(id=entry_id)
    denman = entry.denman
    if request.method == 'POST':
        entry.delete()
        return redirect('unit_logs:denman', denman_id=denman.id)

# Edit kauto entry pages
@xframe_options_exempt
@login_required
def edit_kauto_entry(request, entry_id):
    """Edit an exiting kauto entry"""
    entry = Kauto_Entry.objects.get(id=entry_id)
    kauto = entry.kauto

    if request.method != 'POST':
        form = KautoEntryForm(instance=entry)
    else:
        form = KautoEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:kauto', kauto_id=kauto.id)

    context = {'entry': entry, 'kauto': kauto, 'form': form}
    return render(request, 'unit_logs/edit_kauto_entry.html', context)

@xframe_options_exempt
@login_required
def delete_kauto_entry(request, entry_id):
    entry = Kauto_Entry.objects.get(id=entry_id)
    kauto = entry.kauto
    if request.method == 'POST':
        entry.delete()
        return redirect('unit_logs:kauto', kauto_id=kauto.id)

# Edit frankel entry pages
@xframe_options_exempt
@login_required
def edit_frankel_entry(request, entry_id):
    """Edit an exiting frankel entry"""
    entry = Frankel_Entry.objects.get(id=entry_id)
    frankel = entry.frankel

    if request.method != 'POST':
        form = FrankelEntryForm(instance=entry)
    else:
        form = FrankelEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:frankel', frankel_id=frankel.id)

    context = {'entry': entry, 'frankel': frankel, 'form': form}
    return render(request, 'unit_logs/edit_frankel_entry.html', context)

@xframe_options_exempt
@login_required
def delete_frankel_entry(request, entry_id):
    entry = Frankel_Entry.objects.get(id=entry_id)
    frankel = entry.frankel
    if request.method == 'POST':
        entry.delete()
        return redirect('unit_logs:frankel', frankel_id=frankel.id)


# Edit other entry pages
@xframe_options_exempt
@login_required
def edit_other_entry(request, entry_id):
    """Edit an exiting other entry"""
    entry = Other_Entry.objects.get(id=entry_id)
    other = entry.other

    if request.method != 'POST':
        form = OtherEntryForm(instance=entry)
    else:
        form = OtherEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_logs:other', other_id=other.id)

    context = {'entry': entry, 'other': other, 'form': form}
    return render(request, 'unit_logs/edit_other_entry.html', context)

@xframe_options_exempt
@login_required
def delete_other_entry(request, entry_id):
    entry = Other_Entry.objects.get(id=entry_id)
    other = entry.other
    if request.method == 'POST':
        entry.delete()
        return redirect('unit_logs:other', other_id=other.id)
