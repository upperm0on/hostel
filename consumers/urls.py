from django.urls import path 

from .views import create_consumer, read_consumer, delete_consumer

urlpatterns = [
    path('create_consumer/', create_consumer, name="create_consumer"),
    path('read_consumer/', read_consumer, name="read_consumer"),
    path('delete_consumer/', delete_consumer, name="delete_consumer"),
]
