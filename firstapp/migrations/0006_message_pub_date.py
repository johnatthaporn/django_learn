# Generated by Django 3.1 on 2020-08-30 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 15, 2, 43, 274218, tzinfo=utc)),
        ),
    ]