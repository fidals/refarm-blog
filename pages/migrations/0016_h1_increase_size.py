# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-20 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_add_validation_to_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='h1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.TextField(db_index=True, default='', verbose_name='name'),
        ),
    ]
