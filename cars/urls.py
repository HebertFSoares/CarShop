from django.urls import path,include
from . import views
urlpatterns = [
    path('cars_list/', views.cars_view, name="cars_list"),
    path('new_car/', views.new_car, name="new_car"),
    
]