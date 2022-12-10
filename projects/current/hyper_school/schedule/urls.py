from django.urls import path

from . import views

app_name = "schedule"
urlpatterns = [
    path('schedule/main/', views.IndexView.as_view(), name="main"),
    path('schedule/course_details/<int:pk>', views.CourseInfoView.as_view(),
         name="course_info"),
    path('schedule/teacher_details/<int:pk>', views.TeacherInfoView.as_view(),
         name="teacher_info"),
    path('', views.root_redirect),
    path('schedule', views.root_redirect),
    path('schedule/index', views.root_redirect),
]
