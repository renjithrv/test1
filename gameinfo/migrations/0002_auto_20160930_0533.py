# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameDay',
            new_name='Day',
        ),
        migrations.RenameModel(
            old_name='GameDetails',
            new_name='Details',
        ),
        migrations.RenameModel(
            old_name='GameLevel',
            new_name='Level',
        ),
        migrations.RenameModel(
            old_name='GameType',
            new_name='Type',
        ),
    ]