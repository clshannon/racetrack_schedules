# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160802_0501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='start_datetime',
        ),
        migrations.AddField(
            model_name='event',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
