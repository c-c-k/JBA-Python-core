from django.urls import path

from . import views

app_name = "hypergift"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("custom_form", views.PostcardCustomFormView.as_view(),
         name="custom_form_view"),
    path("model_form", views.PostcardModelFormView.as_view(),
         name="model_form_view"),
]
