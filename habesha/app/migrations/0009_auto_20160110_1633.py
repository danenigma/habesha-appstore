# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160110_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appprofile',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
