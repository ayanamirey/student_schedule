# Generated by Django 4.0.6 on 2022-08-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_pair_time_delete_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pair',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='pair',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='pair',
            name='time',
        ),
    ]
