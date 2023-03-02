from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Add other URL patterns for your app here
]