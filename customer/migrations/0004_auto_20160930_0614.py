# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20160930_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]
