# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-08 03:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0031_auto_20180208_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulestep',
            name='duration',
            field=models.IntegerField(default=4, help_text='The duration in weeks', validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(52)], verbose_name='Duration'),
        ),
    ]
