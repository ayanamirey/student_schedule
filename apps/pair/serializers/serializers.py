from rest_framework import serializers
from pair.models.models import Pair
from teacher.serializers.serializers import TeacherSerializer
from subject.serializers.serializers import SubjectSerializer
from time_pair.serializers.serializers import TimeSerializer


class PairSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    subject = SubjectSerializer()
    time = TimeSerializer()

    class Meta:
        model = Pair
        fields = '__all__'
