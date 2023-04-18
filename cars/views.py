from django.shortcuts import render,redirect
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
    if request.method == "POST":
        new_car_form = CarFrom(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars/cars_list/')
        
    else:
        new_car_form = CarFrom()
    return render(request, 'new_cars.html',{'new_car_form': new_car_form})
        
