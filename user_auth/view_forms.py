from django import forms 

class View_user_signup(forms.Form): 
    name    = forms.CharField(max_length=244, widget=forms.TextInput(
        attrs = {
            'type' : 'text',
            'autofocus': '',
        }
    )) 
    email   = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'type' : 'password'
        }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'type' : 'password',
            'required': '',
        }
    )) 

class View_user_login(forms.Form): 
    name   = forms.CharField(max_length=244, widget=forms.TextInput(
        attrs = {
            'type' : 'text',
            'autofocus': '',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'type' : 'password'
        }
    ))