# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-01 05:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0014_auto_20180901_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 1, 5, 24, 8, 666160, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mfg_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 1, 5, 24, 8, 666160, tzinfo=utc)),
        ),
    ]
