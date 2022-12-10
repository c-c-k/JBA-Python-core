from django.views.generic import DetailView
from django.shortcuts import render, redirect, reverse
from django.views import View

from .models import Teacher, Student, Course


def root_redirect(request):
    return redirect(reverse("schedule:main"), permanent=True)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        try:
            search_term = request.GET['q']
        except KeyError:
            search_term = None
        if search_term:
            courses = Course.objects.filter(title__contains=search_term)
        else:
            courses = Course.objects.all()
        context = {
            'courses': courses,
        }
        return render(request, "schedule/index.html", context)


class CourseInfoView(DetailView):
    model = Course
    template_name = "schedule/course_info.html"


class TeacherInfoView(DetailView):
    model = Teacher
    template_name = "schedule/teacher_info.html"


