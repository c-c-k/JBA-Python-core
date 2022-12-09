from django.db import models


class PersonCommonInfo(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Teacher(PersonCommonInfo):
    about = models.TextField()


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=1024)
    duration_months = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    teacher = models.ManyToManyField(Teacher)


class Student(PersonCommonInfo):
    course = models.ManyToManyField(Course)
