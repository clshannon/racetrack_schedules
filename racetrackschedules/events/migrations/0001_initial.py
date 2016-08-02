# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('racetracks', '0005_racetrack_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('racetrack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racetracks.Racetrack')),
            ],
        ),
    ]