# Generated by Django 4.2.2 on 2023-08-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_auth', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_uploader',
            field=models.BooleanField(default=False),
        ),
    ]
