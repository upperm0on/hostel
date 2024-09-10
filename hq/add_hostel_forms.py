from .models import Hostel

from django import forms

class Views_addHostel(forms.ModelForm): 
    class Meta: 
        model = Hostel 
        fields = ["name", "location", "category", "image"]


