from django.db import models


class Time(models.Model):
    time = models.CharField('Время начало пары', max_length=16)

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'

    def __str__(self):
        return self.time
