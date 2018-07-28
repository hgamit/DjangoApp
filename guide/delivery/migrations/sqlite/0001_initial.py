# Generated by Django 2.0.2 on 2018-07-16 17:30

import delivery.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pic', models.FileField(default='image.jpg', upload_to=delivery.models.user_directory_path)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Please make sure phone number format: '+199999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Transgender')], max_length=11)),
                ('date_of_birth', models.DateField(max_length=8)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
