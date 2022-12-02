from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='tournament_index'),
    re_path(r'(?P<team_id>\d+/?)', views.TeamView.as_view(),
            name='tournament_team'),
]
