# Generated by Django 4.2.2 on 2023-07-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesite', '0005_alter_moviemodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
