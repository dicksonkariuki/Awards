# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20181118_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='creativity',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='design',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='overall_score',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='usability',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
