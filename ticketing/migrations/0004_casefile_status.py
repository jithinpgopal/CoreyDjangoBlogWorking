# Generated by Django 2.1.6 on 2019-03-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_delivery_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='casefile',
            name='status',
            field=models.CharField(choices=[('new', 'NEW'), ('accepted', 'ACCEPTED'), ('completed', 'COMPLETED'), ('overdue', 'OVERDUE')], default='completed', max_length=6),
        ),
    ]
