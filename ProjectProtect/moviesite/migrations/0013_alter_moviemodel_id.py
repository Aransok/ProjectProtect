# Generated by Django 4.2.2 on 2023-07-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesite', '0012_alter_moviemodel_id_alter_moviemodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
