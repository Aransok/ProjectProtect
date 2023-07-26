from random import choices

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    GENDER_CHOICES =[
        ('Male', 'Male'),
        ('Female', 'Female'),
]
    first_name = models.CharField(max_length=30 , null=True, blank=True)
    last_name = models.CharField(max_length=30 , null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='static/images/profile/')
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)