# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-05 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_userhash'),
    ]

    operations = [
        migrations.AddField(
            model_name='fingouser',
            name='cover_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='fingouser',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='fingouser',
            name='is_facebook',
            field=models.BooleanField(default=False),
        ),
    ]
