# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0005_auto_20160325_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='side',
            field=models.BooleanField(choices=[(True, 'Groom'), (False, 'Bride')]),
        ),
    ]