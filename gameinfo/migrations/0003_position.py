# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0002_auto_20160930_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(choices=[(b'NONE', b'None'), (b'FORWARD', b'Forward'), (b'DEFENDER', b'Defender'), (b'GOALKEEPER', b'Goalkeeper'), (b'MIDFIELDER', b'Midfielder')], default=b'NONE', max_length=100)),
                ('gamedetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameinfo.Details')),
            ],
        ),
    ]
