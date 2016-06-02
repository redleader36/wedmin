# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0002_auto_20160601_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='invites',
            new_name='invite',
        ),
        migrations.AlterField(
            model_name='invite',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='weddings.Event'),
        ),
        migrations.AlterField(
            model_name='invite',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='weddings.Guest'),
        ),
    ]