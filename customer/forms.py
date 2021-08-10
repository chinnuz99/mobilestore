from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields=["first_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())

