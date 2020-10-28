# Generated by Django 3.1.1 on 2020-10-21 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0007_auto_20201021_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerevent',
            name='cover',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 11, 16, 34, 62232)),
        ),
    ]
