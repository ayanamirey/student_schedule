# Generated by Django 4.0.6 on 2022-08-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfTheWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('понедельник', 'понедельник'), ('вторник', 'вторник'), ('среда', 'среда'), ('четверг', 'четверг'), ('пятница', 'пятница')], default='1', max_length=100, verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дни',
            },
        ),
    ]