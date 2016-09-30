# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('gameinfo', '0002_auto_20160930_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buddy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buddyname', models.CharField(max_length=100)),
                ('buddyemail', models.EmailField(max_length=150)),
                ('buddycell', models.CharField(max_length=10)),
                ('gamedetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameinfo.Details')),
            ],
        ),
        migrations.CreateModel(
            name='BuddyRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sessionrating', models.IntegerField()),
                ('timemanagement', models.BooleanField()),
                ('warmup', models.BooleanField()),
                ('matchquality', models.BooleanField()),
                ('sessionissues', models.BooleanField()),
                ('sessioncomments', models.TextField()),
                ('buddyrating', models.IntegerField()),
                ('communication', models.BooleanField()),
                ('attire', models.BooleanField()),
                ('gameknowledge', models.BooleanField()),
                ('buddyissue', models.BooleanField()),
                ('buddycomments', models.TextField()),
                ('bookingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.BookingLog')),
                ('buddy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy.Buddy')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rolename', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='buddy',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy.Role'),
        ),
    ]