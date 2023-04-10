from django.urls import path,include
from . import views
urlpatterns = [
    path('my_cars/', views.cars_view, name="cars_list"),
]