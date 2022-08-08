# Generated by Django 4.0.6 on 2022-08-04 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_pair', '0001_initial'),
        ('app', '0012_alter_pair_subject_delete_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='time_pair.time', verbose_name='Время'),
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]