from django.shortcuts import render,redirect
from django.urls import reverse
from cars.models import Car
from .forms import CarModelForm 
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        
        if search:
            cars = Car.objects.filter(model__icontains=search)
        return cars
    
        
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
    
class NewCarCreateView(CreateView):
    model = 'car'
    form_class = CarModelForm
    template_name = 'new_cars.html'
    success_url = reverse_lazy('cars_list')
    
class CarDetailView(DetailView):
    model = Car
    template_namem = 'car_detail.html'
    