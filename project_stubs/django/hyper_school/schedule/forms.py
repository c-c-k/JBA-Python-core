from django.forms import ModelForm

from .models import Student


class StudentApplyToCourseModelForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'age', 'course')
