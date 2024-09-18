from django.urls import path 
from .views import add_hostel, read_hostel, update_hostel, search_hostel, detail_hostel, room_details

urlpatterns = [
    path('add_hostel/', add_hostel, name="add_hostel"),
    path('update_hostel/<int:id>/', update_hostel, name="update_hostel"),
    path('read_hostel/', read_hostel, name="read_hostels"),
    path('search_hostel/<int:rooms>/', search_hostel, name="search_hostel"),
    path('detail_hostel/<int:id>/', detail_hostel, name="detail_hostel"),
    path('room_details/<str:name>/', room_details, name="room_detail")
]
