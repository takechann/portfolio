# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_auto_20170316_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='add_date',
        ),
    ]
