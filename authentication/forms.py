from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))


    class Meta:
        model=User
        fields=('username','password1','email','password2')