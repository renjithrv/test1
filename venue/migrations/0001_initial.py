# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
        ('gameinfo', '0002_auto_20160930_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('venuename', models.CharField(max_length=100)),
                ('venuepic', models.ImageField(upload_to=b'')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10, max_length=8)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11, max_length=8)),
                ('logicalarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.LogicalArea')),
            ],
        ),
        migrations.CreateModel(
            name='VenueGamesAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gamedetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameinfo.Details')),
                ('venuedetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.VenueDetails')),
            ],
        ),
    ]
