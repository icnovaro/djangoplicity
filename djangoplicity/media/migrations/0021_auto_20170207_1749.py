# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-07 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0020_auto_20170207_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='fov_x_l',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'Horizontal Field of View (west), in degrees', max_digits=5, null=True, verbose_name=b'FOV x West'),
        ),
        migrations.AlterField(
            model_name='image',
            name='fov_x_r',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'Horizontal Field of View (east), in degrees', max_digits=5, null=True, verbose_name=b'FOV x East'),
        ),
        migrations.AlterField(
            model_name='image',
            name='fov_y_d',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'Vertical Field of View (bottom), in degrees', max_digits=5, null=True, verbose_name=b'FOV y Bottom'),
        ),
        migrations.AlterField(
            model_name='image',
            name='fov_y_u',
            field=models.DecimalField(blank=True, decimal_places=2, help_text=b'Vertical Field of View (top), in degrees', max_digits=5, null=True, verbose_name=b'FOV y Top'),
        ),
    ]
