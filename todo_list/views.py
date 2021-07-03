from django.shortcuts import render, redirect
from .forms import Listform, WorkVolumeform
from .models import list, Work_Volume
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
        return render(request, 'work_volume/work_volume_create.html', {'work_volume_items': work_volume_items})
    else:
        work_volume_items = Work_Volume.objects.all
        return render(request, 'work_volume/work_volume_create.html', {'work_volume_items': work_volume_items})
