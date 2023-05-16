from django.urls import path,include
from . import views
urlpatterns = [
    path('cars_list/', views.CarsListView.as_view() , name="cars_list"),
    path('new_car/', views.NewCarCreateView.as_view(), name="new_car"),
    
]