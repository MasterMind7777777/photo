from django.shortcuts import render
from .models import Photo
from django.views.generic import ListView, DetailView

class PhotoListView(ListView):
    model = Photo
    template_name = 'photoCatalog/photo_list.html'
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'
    context_object_name = 'photo'