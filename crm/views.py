from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.test import Client

from crm.forms import *
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('crm:home')
    else:
        form = OrderForm()
    orders = CRUDModel.objects.filter(user=request.user)
    return render(request, 'crm/home.html', {'form': form, 'orders': orders})


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('crm:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'crm/profile.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('crm:home')
    else:
        form = RegisterForm()
    return render(request, 'crm/registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crm:home')
        else:
            messages.error(request, 'Username or password is incorrect.')
    return render(request, 'registration/login.html')


def settings(request):
    user = request.user
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('crm:profile')
    else:
        form = SettingsForm(instance=user)
    return render(request, 'crm/settings.html', {'form': form})

def orders_view(request):
    context = {
        'orders' : CRUDModel.objects.all()
    }
    return render(request, 'crm/Dashboard.html', context)

def delete_order(request, order_id):
    order = get_object_or_404(CRUDModel, id=order_id)
    if request.method == "POST":
        order.delete()
        return redirect('crm:home')
    return render(request, 'crm/delete_order.html', {'order': order})

def clients_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:clients')
    else:
        form = ClientForm()
    clients = ClientModel.objects.all()
    return render(request, 'crm/clients.html', {'form': form, 'clients': clients})

def edit_client(request, client_id):
    client = get_object_or_404(ClientModel, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('crm:clients')
    return redirect('crm:clients')

def delete_client(request, client_id):
    client = get_object_or_404(ClientModel, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('crm:clients')
    return redirect('crm:clients')