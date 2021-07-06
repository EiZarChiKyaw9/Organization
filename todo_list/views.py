from django.shortcuts import render, redirect
from .forms import Listform, WorkVolumeform, SlabLevelForm, SiteForm, WVMainForm, WVDailyReportDetailsForm
from .models import list, Work_Volume, Slab_Level, Site, WV_Main, WV_Daily_Report_Details
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.method == 'POST':
        form = Listform(request.POST or None)
        if form.is_valid():
            form.save()

        all_items = list.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('home')


def cross_off(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = True
    item.save()
    all_items = list.objects.all
    return redirect('home')

def uncross(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()
    all_items = list.objects.all
    return redirect('home')

def edit(request, list_id ):

    if request.method == 'POST':
        item = list.objects.get(pk=list_id)


        form = Listform(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been updated!'))
            return redirect('home')

    else:
        item = list.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


def logon(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('successful login!'))
            return redirect('home')
        else:
            messages.success(request, ('Wrong username and password!'))
            return redirect('logon')
    else:
        return render(request, 'authenticate/User_Logon.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('logon')


def work_volume(request):
    if request.method == 'POST':
        form = WorkVolumeform(request.POST or None)
        if form.is_valid():
            form.save()

        work_volume_items = Work_Volume.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'admin/work_volume_create.html', {'work_volume_items': work_volume_items})
    else:
        work_volume_items = Work_Volume.objects.all
        return render(request, 'admin/work_volume_create.html', {'work_volume_items': work_volume_items})


def slab_level(request):
    if request.method == 'POST':
        form = SlabLevelForm(request.POST or None)
        if form.is_valid():
            form.save()

        slab_level_items = Slab_Level.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'admin/slab_level_create.html', {'slab_level_items': slab_level_items})
    else:
        slab_level_items = Slab_Level.objects.all
        return render(request, 'admin/slab_level_create.html', {'slab_level_items': slab_level_items})


def site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST or None)
        if form.is_valid():
            form.save()

        site_items = Site.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'admin/site_create.html', {'site_items': site_items})
    else:
        site_items = Site.objects.all
        return render(request, 'admin/site_create.html', {'site_items': site_items})


def wv_main(request):
    if request.method == 'POST':
        form = WVMainForm(request.POST or None)
        if form.is_valid():
            form.save()

        wv_main_items = WV_Main.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'submission/wv_submit_report.html', {'wv_main_items': wv_main_items})
    else:
        wv_main_items = WV_Main.objects.all
        return render(request, 'submission/wv_submit_report.html', {'wv_main_items': wv_main_items})


def daily_wv_submission(request, site_id):

    if request.method == 'POST':

        form = WVDailyReportDetailsForm(request.POST or None)
        if form.is_valid():
            form.save()

        Daily_report_Details_item = WV_Daily_Report_Details.objects.all
        wv_main_item = WV_Main.objects.get(pk=site_id)
        work_volume_items = Work_Volume.objects.all
        slab_level_items = Slab_Level.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'submission/submit_daily_workvolume.html',
                      {'Daily_report_Details_items': Daily_report_Details_item,
                       'wv_main_item': wv_main_item,
                       'work_volume_items': work_volume_items,
                       'slab_level_items': slab_level_items})

    else:
        wv_main_item = WV_Main.objects.get(pk=site_id)
        work_volume_items = Work_Volume.objects.all
        slab_level_items = Slab_Level.objects.all
        Daily_report_Details_items = WV_Daily_Report_Details.objects.all
        return render(request, 'submission/submit_daily_workvolume.html',
                      {'Daily_report_Details_items': Daily_report_Details_items,
                       'wv_main_item': wv_main_item,
                       'work_volume_items': work_volume_items,
                       'slab_level_items': slab_level_items})
