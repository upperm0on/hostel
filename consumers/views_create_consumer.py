from django import forms 
from .models import Consumer

class Views_create_consumer(forms.ModelForm): 
    class Meta: 
        model = Consumer
        fields = ['name', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            'type': 'password',
        }
    ))