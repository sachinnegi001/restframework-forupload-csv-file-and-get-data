# Generated by Django 4.0.3 on 2022-09-28 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_ratings_moviess'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='moviess',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datta', to='app.movies'),
        ),
    ]
