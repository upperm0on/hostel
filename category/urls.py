from django.urls import path 
from .views import create_category

urlpatterns = [
    path('create_category/', create_category, name="create_category"),
]
