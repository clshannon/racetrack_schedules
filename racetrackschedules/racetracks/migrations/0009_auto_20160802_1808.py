# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetracks', '0008_auto_20160802_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racetrack',
            name='main_phone',
            field=models.IntegerField(blank=True, max_length=16, null=True),
        ),
    ]