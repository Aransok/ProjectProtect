from django.forms import forms, ModelForm
from django import forms
from django.shortcuts import redirect, render

from ProjectProtect.moviesite.models import MovieModel, Comment


class MovieModelForm(ModelForm):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Fantasy', 'Fantasy'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Horror', 'Horror'),
        ('Crime', 'Crime'),
        ('Drama', 'Drama'),
        ('Animation', 'Animation'),
        ('Thriller', 'Thriller'),
        ('Mistery', 'Mistery'),
    ]
    genre = forms.MultipleChoiceField(choices=GENRE_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = MovieModel
        fields = '__all__'
        exclude = ['slug']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
