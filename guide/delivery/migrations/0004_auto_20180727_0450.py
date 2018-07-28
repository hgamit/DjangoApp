# Generated by Django 2.0.2 on 2018-07-27 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20180726_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address_type',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Communication', 'Communication'), ('Receiver', 'Receiver')], default='Communication', max_length=13),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='uaddress', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='po_box_number',
            field=models.CharField(max_length=255),
        ),
    ]
