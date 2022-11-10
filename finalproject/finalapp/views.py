from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy

from .models import Person, Branch
from .forms import PersonForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django import forms

class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    # success_url = reverse_lazy('person_changelist')
    success_url = reverse_lazy('application_accepted')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'finalapp/branch_dropdown_list_options.html', {'branches': branches})

def logout(request):
    auth.logout(request)
    return login(request)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/finalapp')
        else:
            messages.info(request, "invalid credentials")
            return render(request, 'finalapp/login.html')

    return render(request, 'finalapp/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                # return redirect('register')
                return render(request, 'finalapp/register.html')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                request.method = 'GET'
                return redirect(login)


        else:
            messages.info(request, "password not matching")
            return render(request, 'finalapp/register.html')

    return render(request, 'finalapp/register.html')


def application_accepted(request):
    return render(request,'application_accepted.html')
