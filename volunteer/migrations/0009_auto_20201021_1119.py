# Generated by Django 3.1.1 on 2020-10-21 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0008_auto_20201021_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerevent',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 11, 19, 6, 798167)),
        ),
    ]
