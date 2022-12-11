from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, FormView, CreateView
from django.urls import reverse, reverse_lazy

from .forms import StudentApplyToCourseModelForm
from .models import Teacher, Student, Course


def root_redirect(request):
    return redirect(reverse("schedule:main"), permanent=True)


def student_signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # login(request, user)
            return redirect('schedule:main')
        else:  # submitted registration data is invalid
            pass  # maybe add some extra error messages
    else:  # request method is not POST
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'schedule/student_sign_up.html', context)


class StudentLoginView(LoginView):
    template_name = 'schedule/student_login.html'
    next_page = reverse_lazy('schedule:main')
    # def post(self, request, *args, **kwargs):
    #     response = super().post(request, *args, **kwargs)
    #     print(response.url)
    #     return response


class StudentLogoutView(LogoutView):
    next_page = reverse_lazy('schedule:main')


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
            'user': request.user,
            'courses': courses,
        }
        return render(request, "schedule/index.html", context)


class CourseInfoView(DetailView):
    model = Course
    template_name = "schedule/course_info.html"


class TeacherInfoView(DetailView):
    model = Teacher
    template_name = "schedule/teacher_info.html"


class JoinCourseView(CreateView):
    form_class = StudentApplyToCourseModelForm
    template_name = "schedule/student_enroll_to_course_form.html"
    success_url = reverse_lazy("schedule:join_course")


