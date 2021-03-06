# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-29 13:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0007_auto_20180828_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2018, 8, 29, 13, 21, 50, 142902, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mfg_date',
            field=models.DateField(default=datetime.datetime(2018, 8, 29, 13, 21, 50, 142902, tzinfo=utc)),
        ),
    ]
