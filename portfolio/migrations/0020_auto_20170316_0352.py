# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20170316_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
