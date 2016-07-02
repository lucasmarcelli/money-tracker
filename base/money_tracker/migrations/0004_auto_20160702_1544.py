# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_tracker', '0003_auto_20160702_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line',
            old_name='amount',
            new_name='amount_in',
        ),
        migrations.AddField(
            model_name='line',
            name='amount_out',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
