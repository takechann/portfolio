# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_product_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(default='date published', verbose_name='date published'),
        ),
    ]
