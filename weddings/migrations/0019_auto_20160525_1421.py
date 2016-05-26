# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0018_auto_20160525_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodging',
            name='event',
        ),
        migrations.RemoveField(
            model_name='registry',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lodging',
            name='events',
            field=models.ManyToManyField(to='weddings.Event'),
        ),
        migrations.AddField(
            model_name='lodging',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='registry',
            name='events',
            field=models.ManyToManyField(to='weddings.Event'),
        ),
    ]
