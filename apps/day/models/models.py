from django.db import models

DAY_OF_THE_WEEK = (
    ('понедельник', 'понедельник'),
    ('вторник', 'вторник'),
    ('среда', 'среда'),
    ('четверг', 'четверг'),
    ('пятница', 'пятница'),
)


class DayOfTheWeek(models.Model):
    name = models.CharField('День недели',
                            max_length=100,
                            choices=DAY_OF_THE_WEEK,
                            default='1'
                            )

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    def __str__(self):
        return self.name
