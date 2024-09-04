from django.urls import path 
from .views import create_manager, read_manager, update_manager, delete_manager

urlpatterns = [
    path('create_manager/', create_manager, name="create_manager"),
    path('read_manager/', read_manager, name="read_manager"),
    path('update_manager/<int:id>/', update_manager, name="update_manager"),
    path('delete_manager/', delete_manager, name="delete_manager")
]