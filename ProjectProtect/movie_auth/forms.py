from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth.models import User

from ProjectProtect.movie_auth.models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'date_of_birth': forms.widgets.DateInput(attrs={'type': 'date'}),
            'is_uploader': forms.widgets.CheckboxInput(attrs={'class': 'custom-checkbox'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_uploader'].widget = forms.CheckboxInput(attrs={'class': 'custom-checkbox'})
        if self.instance.is_uploader:
            self.fields['is_uploader'].label = 'Stop Being Uploader'
        else:
            self.fields['is_uploader'].label = 'Become Uploader'
