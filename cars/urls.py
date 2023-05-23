from django.urls import path,include
from . import views

urlpatterns = [
    path('cars_list/', views.CarsListView.as_view() , name="cars_list"),
    path('new_car/', views.NewCarCreateView.as_view(), name="new_car"),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name="car_detail"),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view(), name="car_update"),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(), name="car_delete"),
]