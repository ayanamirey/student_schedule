# Generated by Django 4.0.6 on 2022-08-04 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='group.group'),
        ),
    ]
