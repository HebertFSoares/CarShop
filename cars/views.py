from django.shortcuts import render,redirect
from django.urls import reverse
from cars.models import Car
from .forms import CarModelForm 
from django.views import View

def cars_view(request):
    pass
    '''
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
    
def new_car(request):
    if request.method == "POST":
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect(reverse('cars_list'))
        
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_cars.html',{'new_car_form': new_car_form})
        
