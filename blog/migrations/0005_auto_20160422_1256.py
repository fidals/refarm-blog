# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160422_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('article', 'Статьи'), ('news', 'Новости'), ('navigation', 'Навигация')], default='article', max_length=100),
        ),
    ]
