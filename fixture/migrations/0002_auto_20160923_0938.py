# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='improve_game_slot_details',
            name='improve_fixture_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='improve_game_slot_details',
            name='improve_game_max_players',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='improve_game_slot_details',
            name='improve_home_batch_takein',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='improve_game_slot_details',
            name='improve_no_buddy_required',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='improve_game_slot_details',
            name='improve_venue_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_assigned_buddy1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_assigned_buddy2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_fixture_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_game_max_players',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_home_batch_takein',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_temp_buddy1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_temp_buddy2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='play_game_slot_details',
            name='play_venue_id',
            field=models.IntegerField(),
        ),
    ]
