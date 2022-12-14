# Generated by Django 4.0.3 on 2022-09-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconts', models.CharField(blank=True, max_length=500, null=True)),
                ('titleType', models.CharField(blank=True, max_length=500, null=True)),
                ('primaryTitle', models.CharField(blank=True, max_length=50, null=True)),
                ('runtimeMinutes', models.IntegerField()),
                ('genres', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('averageRating', models.FloatField()),
                ('tconst', models.IntegerField()),
            ],
        ),
    ]
