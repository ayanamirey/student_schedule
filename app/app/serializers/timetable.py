from rest_framework import serializers
from app.models.timetable import Pair
from authorization.models.users import MyUser
from .any_serializers import DaySerilaizer, GroupSerilaizer, LessonSerilaizer


class PairSerializer(serializers.ModelSerializer):
    day = DaySerilaizer()
    group = GroupSerilaizer()
    lessons = LessonSerilaizer(many=True)

    class Meta:
        model = Pair
        fields = '__all__'


class PairCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'


class MyUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('group',)
