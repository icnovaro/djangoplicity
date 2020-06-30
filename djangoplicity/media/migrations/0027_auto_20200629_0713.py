# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 07:13
from __future__ import unicode_literals

from django.db import migrations
import djangoplicity.metadata.archives.fields


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0026_auto_20190311_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='type',
            field=djangoplicity.metadata.archives.fields.AVMTypeField(blank=True, choices=((b'Observation', 'Observation'), (b'Artwork', 'Artwork'), (b'Photographic', 'Photographic'), (b'Planetary', 'Planetary'), (b'Simulation', 'Simulation'), (b'Collage', 'Collage'), (b'Chart', 'Chart'), (b'Nightscape', 'Nightscape'), (b'Day Photo', 'Day Photo'), (b'DeepSky Photo', 'DeepSky Photo'), (b'Spectrum', 'Spectrum'), (b'Annotated Obs', 'Annotated Observation')), help_text='The type of image/media resource.', max_length=30, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='video',
            name='type',
            field=djangoplicity.metadata.archives.fields.AVMTypeField(blank=True, choices=((b'Observation', 'Observation'), (b'Artwork', 'Artwork'), (b'Photographic', 'Photographic'), (b'Planetary', 'Planetary'), (b'Simulation', 'Simulation'), (b'Collage', 'Collage'), (b'Chart', 'Chart'), (b'Nightscape', 'Nightscape'), (b'Day Photo', 'Day Photo'), (b'DeepSky Photo', 'DeepSky Photo'), (b'Spectrum', 'Spectrum'), (b'Annotated Obs', 'Annotated Observation')), help_text='The type of image/media resource.', max_length=30, null=True, verbose_name='Type'),
        ),
    ]