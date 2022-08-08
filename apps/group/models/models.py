from django.db import models


class Group(models.Model):
    name = models.CharField('Номер группы', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
