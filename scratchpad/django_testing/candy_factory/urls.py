from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.CandyFactoryIndex.as_view(), name="candy_factory_index"),
    re_path(r'(?P<candy_name>[^/]+)/?', views.CandyInfo.as_view(),
            name="candy_info")
]