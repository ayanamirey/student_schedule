# Generated by Django 4.0.6 on 2022-08-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_group_name_alter_subject_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10, verbose_name='Время пары')),
            ],
        ),
        migrations.RenameModel(
            old_name='Day',
            new_name='DayOfTheWeek',
        ),
    ]