
from rest_framework import serializers
from main.models import Teacher, Subject


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name']
        

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class SubjectDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherListSerializer(read_only=True, many=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'name', 'teachers']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'