# Generated by Django 5.0.6 on 2024-09-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
