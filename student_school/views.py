from rest_framework import viewsets
from .serializers import StudentSerializer, SchoolSerializer, StudentSchoolSerializer
from .models import School, Student


# Create your views here.

class SchoolView(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return School.objects.all()


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class StudentSchoolView(viewsets.ModelViewSet):
    serializer_class = StudentSchoolSerializer

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])
