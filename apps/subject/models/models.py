from django.db import models


class Subject(models.Model):
    name = models.CharField('Предмет', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
