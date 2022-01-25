from rest_framework import serializers
from .models import Student, School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class StudentSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('school',)

    def create(self, validated_data):
        school = School.objects.get(pk=self.context['view'].kwargs['school_pk'])
        validated_data['school'] = school
        return super(StudentSchoolSerializer, self).create(validated_data)
