# Generated by Django 4.2.16 on 2024-11-05 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='consumer',
            name='password',
        ),
        migrations.AddField(
            model_name='consumer',
            name='account_type',
            field=models.CharField(choices=[('user', 'user'), ('manager', 'manager')], default='user', max_length=255),
        ),
        migrations.AddField(
            model_name='consumer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]