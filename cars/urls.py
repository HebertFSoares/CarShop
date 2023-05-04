from django.urls import path,include
from . import views
urlpatterns = [
    path('cars_list/', views.CarsView.as_view() , name="cars_list"),
    path('new_car/', views.NewCar.as_view(), name="new_car"),
    
]