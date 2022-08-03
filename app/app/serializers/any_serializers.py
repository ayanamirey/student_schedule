from rest_framework import serializers
from app.models.timetable import Lessons, Group, Day, Subject, Teacher


class DaySerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ("__all__")


class GroupSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("__all__")


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("__all__")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("__all__")


class LessonSerilaizer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Lessons
        fields = ("__all__")
