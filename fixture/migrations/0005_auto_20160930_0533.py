# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
        ('buddy', '0001_initial'),
        ('fixture', '0004_auto_20160930_0533'),
        ('booking', '0003_bookinglog_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.VenueDetails'),
        ),
        migrations.AddField(
            model_name='buddyaudit',
            name='buddy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy.Buddy'),
        ),
        migrations.AddField(
            model_name='buddyaudit',
            name='fixture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Fixture'),
        ),
        migrations.AddField(
            model_name='assignedbuddylog',
            name='bookingid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.BookingLog'),
        ),
        migrations.AddField(
            model_name='assignedbuddylog',
            name='buddy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy.Buddy'),
        ),
        migrations.AddField(
            model_name='assignedbuddylog',
            name='fixture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Fixture'),
        ),
        migrations.AddField(
            model_name='assignedbuddy',
            name='buddy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buddy', to='buddy.Buddy'),
        ),
        migrations.AddField(
            model_name='assignedbuddy',
            name='fixture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Fixture'),
        ),
        migrations.AddField(
            model_name='assignedbuddy',
            name='tempbuddy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tempbuddy', to='buddy.Buddy'),
        ),
    ]
