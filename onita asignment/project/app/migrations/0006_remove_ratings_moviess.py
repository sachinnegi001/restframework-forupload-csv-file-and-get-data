# Generated by Django 4.0.3 on 2022-09-28 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_ratings_moviess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='moviess',
        ),
    ]