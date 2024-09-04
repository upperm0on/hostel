from django.urls import path 
from .views import add_hostel, read_hostel, update_hostel

urlpatterns = [
    path('add_hostel/', add_hostel, name="add_hostel"),
    path('update_hostel/<int:id>/', update_hostel, name="update_hostel"),
    path('read_hostel/', read_hostel, name="read_hostels"),
]
