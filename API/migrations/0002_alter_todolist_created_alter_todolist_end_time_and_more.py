# Generated by Django 4.0.5 on 2022-08-21 18:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 8, 21, 18, 58, 50, 596708, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='end_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='start_time',
            field=models.TimeField(auto_now=True),
        ),
    ]