# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographerproduct',
            name='photographer_product_shooting_day',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AddField(
            model_name='photographerproduct',
            name='sort_id',
            field=models.IntegerField(default=0),
        ),
    ]
