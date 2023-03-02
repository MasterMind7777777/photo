from django.urls import path
from .views import PhotoListView, PhotoDetailView

app_name = 'photoCatalog'

urlpatterns = [
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('photos/', PhotoListView.as_view(), name='photos'),
]