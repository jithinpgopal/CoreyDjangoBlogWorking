# Generated by Django 2.1.6 on 2019-03-14 17:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0008_auto_20190314_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casefile',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 13, 17, 50, 13, 155111, tzinfo=utc)),
        ),
    ]