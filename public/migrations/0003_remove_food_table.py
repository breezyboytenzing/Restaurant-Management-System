# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_ordered_food_is_served'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='table',
        ),
    ]
