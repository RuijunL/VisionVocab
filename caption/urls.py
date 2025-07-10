from django.urls import path
from .views import generate_caption

urlpatterns = [
    path('caption/', generate_caption, name = 'generate caption'),
]