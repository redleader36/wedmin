# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-14 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0011_auto_20160609_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestevent',
            name='adults',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='guestevent',
            name='children',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]