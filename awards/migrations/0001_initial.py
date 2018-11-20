# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 19:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colors', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['countries'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('description', tinymce.models.HTMLField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.countries')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('landing_page', models.ImageField(upload_to='landingpage/')),
                ('description', tinymce.models.HTMLField()),
                ('link', models.CharField(max_length=255)),
                ('screenshot1', models.ImageField(upload_to='screenshots/')),
                ('screenshot2', models.ImageField(upload_to='screenshots/')),
                ('screenshot3', models.ImageField(upload_to='screenshots/')),
                ('screenshot4', models.ImageField(upload_to='screenshots/')),
                ('design', models.DecimalField(decimal_places=2, max_digits=2)),
                ('usability', models.DecimalField(decimal_places=2, max_digits=2)),
                ('creativity', models.DecimalField(decimal_places=2, max_digits=2)),
                ('content', models.DecimalField(decimal_places=2, max_digits=2)),
                ('overall_score', models.DecimalField(decimal_places=2, max_digits=2)),
                ('categories', models.ManyToManyField(to='awards.categories')),
                ('colors', models.ManyToManyField(to='awards.colors')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.countries')),
            ],
        ),
        migrations.CreateModel(
            name='technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technologies', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='awards.technologies'),
        ),
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]