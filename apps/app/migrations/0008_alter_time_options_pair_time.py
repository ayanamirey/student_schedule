# Generated by Django 4.0.6 on 2022-08-04 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_pair_subject_alter_pair_teacher_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': 'Время', 'verbose_name_plural': 'Время'},
        ),
        migrations.AddField(
            model_name='pair',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.time', verbose_name='Время'),
        ),
    ]