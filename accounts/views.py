from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    use_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': use_form} )