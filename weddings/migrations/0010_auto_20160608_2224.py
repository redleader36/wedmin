# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-09 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0009_auto_20160608_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='registry/'),
        ),
    ]
