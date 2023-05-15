from django.shortcuts import render,redirect
from django.urls import reverse
from cars.models import Car
from .forms import CarModelForm 
from django.views import View
from django.views.generic import ListView


'''
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    
    if search:
        cars = Car.objects.filter(model__icontains=search)
    
    return render (
        request, 'cars.html',
        {'cars': cars }
    )
'''
class CarsView(View):
    
    def get(self,request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')
    
        if search:
            cars = Car.objects.filter(model__icontains=search)
    
        return render (
            request, 'cars.html',
            {'cars': cars }
     )
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
'''      
def new_car(request):
    if request.method == "POST":
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect(reverse('cars_list'))
        
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_cars.html',{'new_car_form': new_car_form})
'''
        
class NewCar(View):
    
    def get(self,request):
        new_car_form = CarModelForm()
        return render(request, 'new_cars.html',{'new_car_form': new_car_form})

    def post(self,request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect(reverse('cars_list'))
        return render(request, 'new_cars.html',{'new_car_form': new_car_form})