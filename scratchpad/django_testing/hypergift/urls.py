from django.urls import path

from . import views

app_name = "hypergift"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("model_form", views.PostcardFormView.as_view(),
         name="model_form_view")
]
