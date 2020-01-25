# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-27 15:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0004_auto_20180827_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2018, 8, 27, 15, 46, 52, 724396, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='medicines/'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='mfg_date',
            field=models.DateField(default=datetime.datetime(2018, 8, 27, 15, 46, 52, 724396, tzinfo=utc)),
        ),
    ]
