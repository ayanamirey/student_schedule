# Generated by Django 4.0.6 on 2022-08-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pair', '0001_initial'),
        ('app', '0014_remove_pair_subject_remove_pair_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='pair',
            field=models.ManyToManyField(to='pair.pair'),
        ),
        migrations.DeleteModel(
            name='Pair',
        ),
    ]
