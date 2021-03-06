# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_photographerproduct_photographer_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographerproduct',
            name='photographer_main_image',
            field=models.ImageField(blank=True, upload_to=portfolio.models.PhotographerProduct.get_main_image_file_name),
        ),
        migrations.AddField(
            model_name='photographerproduct',
            name='photographer_product_alphabet_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='photographerproduct',
            name='photographer_thumbnail_image',
            field=models.ImageField(blank=True, upload_to=portfolio.models.PhotographerProduct.get_thumbnail_image_file_name),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
