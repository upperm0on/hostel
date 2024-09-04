from django import forms
from .models import Manager

class Views_create_manager(forms.ModelForm):
    class Meta: 
        model = Manager
        fields = ['name', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            'type': 'password',
        }
    ))