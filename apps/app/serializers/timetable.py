from rest_framework import serializers
from app.models.timetable import Timetable
from authorization.models.users import MyUser
from day.serializers.serializers import DayOfTheWeekSerializer
from group.serializers.serializers import GroupSerializer
from pair.serializers.serializers import PairSerializer


class TimetableSerializer(serializers.ModelSerializer):
    day = DayOfTheWeekSerializer()
    group = GroupSerializer()
    pair = PairSerializer(many=True)

    class Meta:
        model = Timetable
        fields = '__all__'


class TimetableCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'


class MyUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('group',)
