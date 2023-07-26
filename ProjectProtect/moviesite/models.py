from enum import unique
from random import choices

from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class MovieModel(models.Model):
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
        ('Adventure', 'Adventure'),
        ('Thriller', 'Thriller'),
        ('Mistery', 'Mistery'),

    ]
    name = models.CharField(max_length=300, blank=False, null=False)
    year = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='static/images/')
    description = models.TextField(max_length=805, null=False, blank=False)
    trailer = models.URLField(null=False, blank=False)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


UserModel = get_user_model()


class Comment(models.Model):
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


