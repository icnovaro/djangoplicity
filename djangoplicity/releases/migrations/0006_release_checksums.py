# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-03 11:22
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0005_auto_20151209_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='checksums',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
