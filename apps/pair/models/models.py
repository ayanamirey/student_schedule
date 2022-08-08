from django.db import models
from subject.models.models import Subject
from teacher.models.models import Teacher
from time_pair.models.models import Time


class Pair(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Предмет', on_delete=models.SET_NULL, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, verbose_name='Имя учителя', on_delete=models.SET_NULL, blank=True, null=True)
    time = models.ForeignKey(Time, verbose_name='Время', on_delete=models.SET_NULL, blank=True, null=True)
    cabinet = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'

    def __str__(self):
        return f'{self.subject} {self.teacher} {self.time} {self.cabinet}'
