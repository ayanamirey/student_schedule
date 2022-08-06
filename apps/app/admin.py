from django.contrib import admin
from app.models.timetable import Timetable
from subject.models.models import Subject
from teacher.models.models import Teacher
from group.models.models import Group
from day.models.models import DayOfTheWeek
from time_pair.models.models import Time
from pair.models.models import Pair

admin.site.register(DayOfTheWeek)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Time)
admin.site.register(Pair)

admin.site.register(Timetable)
