# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingo_statistics', '0002_auto_20161129_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]