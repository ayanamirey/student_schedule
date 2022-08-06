from rest_framework import serializers
from day.models.models import DayOfTheWeek


class DayOfTheWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfTheWeek
        fields = '__all__'
