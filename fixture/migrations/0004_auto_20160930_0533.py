# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0002_auto_20160930_0533'),
        ('fixture', '0003_auto_20160923_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedBuddy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignedBuddyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teamname', models.CharField(max_length=50)),
                ('ratingflag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BuddyAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('startlatitude', models.DecimalField(decimal_places=8, max_digits=10, max_length=8)),
                ('startlongitude', models.DecimalField(decimal_places=8, max_digits=11, max_length=8)),
                ('endlatitude', models.DecimalField(decimal_places=8, max_digits=10, max_length=8)),
                ('endlongitude', models.DecimalField(decimal_places=8, max_digits=11, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gametime', models.TimeField()),
                ('courtname', models.CharField(max_length=50)),
                ('maxplayers', models.IntegerField()),
                ('homebatchtakein', models.IntegerField()),
                ('homebatchstarttime', models.DurationField()),
                ('flexibatchstarttime', models.DurationField()),
                ('generalcutofftime', models.DurationField()),
                ('gameversion', models.IntegerField()),
                ('is_deleted', models.BooleanField()),
                ('gameday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameinfo.Day')),
                ('gamedetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameinfo.Details')),
                ('gametype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameinfo.Type')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameinfo.Level')),
            ],
        ),
        migrations.DeleteModel(
            name='Improve_game_slot_details',
        ),
        migrations.DeleteModel(
            name='Play_game_slot_details',
        ),
    ]
