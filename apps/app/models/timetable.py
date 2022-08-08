from django.db import models
from teacher.models.models import Teacher
from day.models.models import DayOfTheWeek
from group.models.models import Group
from subject.models.models import Subject
from time_pair.models.models import Time
from pair.models.models import Pair


class Timetable(models.Model):
    day = models.ForeignKey(DayOfTheWeek, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    pair = models.ManyToManyField(Pair)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return f'{self.day} - {self.group} группа'


class TimetableTeacher(models.Model):
    day = models.ForeignKey(DayOfTheWeek, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        verbose_name = 'Расписание учителя'
        verbose_name_plural = 'Расписания учителей'