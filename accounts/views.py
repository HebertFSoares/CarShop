from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login
from django.urls import reverse


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/cars/cars_list')
    elif request.method == "GET":
        use_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login(request):
   pass