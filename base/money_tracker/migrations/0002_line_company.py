# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='company',
            field=models.TextField(default='Def'),
            preserve_default=False,
        ),
    ]