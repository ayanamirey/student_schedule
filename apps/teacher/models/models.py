from django.db import models


class Teacher(models.Model):
    name = models.CharField('Имя учителя', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name
