# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-27 10:04
from __future__ import unicode_literals

from django.db import migrations
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20170418_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=images.models.ImageField(upload_to='', verbose_name='image'),
        ),
    ]
