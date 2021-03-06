# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20170324_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_day',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_hour',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_minute',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_month',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_year',
            field=models.CharField(blank=True, default='', max_length=4),
        ),
    ]
