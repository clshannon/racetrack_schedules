# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetracks', '0004_auto_20160802_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='racetrack',
            name='website',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]