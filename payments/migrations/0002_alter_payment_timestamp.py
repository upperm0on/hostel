# Generated by Django 4.2.16 on 2025-02-16 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 16, 0, 55, 7, 616205)),
        ),
    ]
