from django.urls import path 
from .views import create_manager, read_manager, delete_manager, active_listings

urlpatterns = [
    path('create_manager/', create_manager, name="create_manager"),
    path('read_manager/', read_manager, name="read_manager"),
    path('delete_manager/', delete_manager, name="delete_manager"),
    path('active_listings/', active_listings, name="active_listings"),
]