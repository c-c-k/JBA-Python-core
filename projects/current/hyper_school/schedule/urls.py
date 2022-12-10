from django.urls import path

from . import views

app_name = "schedule"
urlpatterns = [
    path('schedule', views.IndexView.as_view(), name="index"),
    path('', views.root_redirect, name="root_redirect"),
]
