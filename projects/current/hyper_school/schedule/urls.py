from django.urls import path

from . import views

app_name = "schedule"
urlpatterns = [
    path('schedule/main/', views.IndexView.as_view(), name="main"),
    path('schedule/course_details/<int:pk>', views.CourseInfoView.as_view(),
         name="course_info"),
    path('schedule/teacher_details/<int:pk>', views.TeacherInfoView.as_view(),
         name="teacher_info"),
    path('schedule/add_course/', views.JoinCourseView.as_view(),
         name="join_course"),
    path('signup/', views.student_signup_view,
         name="student_signup"),
    path('login/', views.StudentLoginView.as_view(),
         name="student_login"),
    path('logout/', views.StudentLogoutView.as_view(),
         name="student_logout"),
    path('', views.root_redirect),
    path('schedule', views.root_redirect),
    path('schedule/index', views.root_redirect),
]
