# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-01 05:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='timestam',
            new_name='timestamp',
        ),
    ]