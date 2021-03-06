# Generated by Django 2.1.6 on 2019-03-14 17:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0005_auto_20190314_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='casefile',
            name='del_group',
            field=models.ForeignKey(default=1, on_delete=models.SET('USER DELETED'), to='ticketing.Delivery_group'),
        ),
        migrations.AlterField(
            model_name='casefile',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 13, 17, 34, 8, 384989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='casefile',
            name='status',
            field=models.CharField(choices=[('new', 'NEW'), ('accepted', 'ACCEPTED'), ('completed', 'COMPLETED'), ('overdue', 'OVERDUE')], default='new', max_length=15),
        ),
    ]
