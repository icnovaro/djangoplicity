# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-27 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0022_auto_20170823_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='frame_rate',
            field=models.PositiveIntegerField(default=30),
        ),
    ]
