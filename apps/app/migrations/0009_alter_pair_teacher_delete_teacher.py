# Generated by Django 4.0.6 on 2022-08-04 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('app', '0008_alter_time_options_pair_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.teacher', verbose_name='Имя учителя'),
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
