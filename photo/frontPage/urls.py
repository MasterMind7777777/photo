from django.urls import path
from . import views

app_name = 'frontPage'

urlpatterns = [
    path('', views.home, name='home'),
    # Add other URL patterns for your app here
]