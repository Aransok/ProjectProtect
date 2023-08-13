from django.forms import forms, ModelForm
from django import forms
from django.shortcuts import redirect, render

from ProjectProtect.moviesite.models import MovieModel, Comment


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = '__all__'
        exclude = ['slug']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
