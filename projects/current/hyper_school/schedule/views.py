from django.shortcuts import render, redirect, reverse
from django.views import View

from .models import Teacher, Student, Course


def root_redirect(request):
    return redirect(reverse("schedule:index"), permanent=True)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "schedule/index.html")
