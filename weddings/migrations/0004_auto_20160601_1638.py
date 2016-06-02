# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0003_auto_20160601_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='invite',
            new_name='invites',
        ),
        migrations.AlterField(
            model_name='invite',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weddings.Event'),
        ),
        migrations.AlterField(
            model_name='invite',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weddings.Guest'),
        ),
    ]