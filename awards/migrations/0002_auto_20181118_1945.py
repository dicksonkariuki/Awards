# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='creativity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='design',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='overall_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='usability',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2),
        ),
    ]
