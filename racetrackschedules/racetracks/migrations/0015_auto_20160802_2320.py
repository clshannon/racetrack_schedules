# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 23:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('racetracks', '0014_tracktypes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrackTypes',
            new_name='SurfaceType',
        ),
    ]
