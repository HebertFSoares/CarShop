from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logout, name="logout")
]
