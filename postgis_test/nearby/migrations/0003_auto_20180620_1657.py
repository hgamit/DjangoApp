# Generated by Django 2.0.2 on 2018-06-20 21:57

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nearby', '0002_auto_20180620_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]
