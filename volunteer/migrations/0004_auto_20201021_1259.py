# Generated by Django 3.1.1 on 2020-10-21 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0003_auto_20201019_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 12, 59, 7, 362635)),
        ),
    ]