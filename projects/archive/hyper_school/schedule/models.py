from django.db import models


class PersonCommonInfo(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def full_name(self):
        return ' '.join((self.name, self.surname))

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

    def enrolled_students(self):
        return self.student_set.all()


class Student(PersonCommonInfo):
    course = models.ManyToManyField(Course)
