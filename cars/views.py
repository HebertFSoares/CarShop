from django.shortcuts import render
from cars.models import Car
from django.http import HttpResponse
from .forms import CarFrom 

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    
    if search:
        cars = Car.objects.filter(model__icontains=search)
    
    return render (
        request, 'cars.html',
        {'cars': cars }
    )

def new_car(request):
    new_car_form = CarFrom()
    return render(request, 'new_cars.html',{'new_car_form': new_car_form})
