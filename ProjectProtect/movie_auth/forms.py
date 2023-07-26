from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
