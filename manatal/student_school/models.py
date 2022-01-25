import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from rest_framework.exceptions import ValidationError


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class School(BaseModel):
    name = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=True)
    maximum_number_of_students = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def student_count(self):
        return self.students.count()

    class Meta:
        db_table = "school"


class Student(BaseModel):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    registration_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students', default=None)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "student"


@receiver(pre_save, sender=Student)
def student_max_limit_check(sender, instance, **kwargs):
    if instance.school.students.count() >= instance.school.maximum_number_of_students:
        raise ValidationError(f'Max limit has been reached for the students in this school')
