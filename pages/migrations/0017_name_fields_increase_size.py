# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-23 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_h1_increase_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='h1',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='page',
            name='menu_title',
            field=models.CharField(blank=True, help_text='This field will be shown in the breadcrumbs, menu items and etc.', max_length=1000, verbose_name='menu title'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=1500, verbose_name='slug'),
        ),
    ]
