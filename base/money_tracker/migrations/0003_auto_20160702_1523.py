# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money_tracker', '0002_line_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line',
            old_name='unneccesary',
            new_name='unnecessary',
        ),
    ]
