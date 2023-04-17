from django.shortcuts import render
from cars.models import Car
from django.http import HttpResponse

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
    if request.method == "GET":
        return HttpResponse("new_cars")
