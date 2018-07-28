# Generated by Django 2.0.2 on 2018-07-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20180726_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='address_type',
            field=models.CharField(choices=[('Permanent', 'Male'), ('Communication', 'Communication'), ('Receiver', 'Receiver')], default='Communication', max_length=13),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='po_box_number',
            field=models.CharField(default='100', max_length=255),
        ),
    ]
