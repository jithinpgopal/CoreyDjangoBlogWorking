# Generated by Django 2.1.6 on 2019-03-20 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0009_auto_20190314_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casefile',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 19, 12, 30, 3, 714133, tzinfo=utc)),
        ),
    ]