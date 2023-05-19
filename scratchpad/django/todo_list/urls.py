from django.urls import path

from .views import TodoView
app_name = "todo_list"
urlpatterns = [
    path("", TodoView.as_view(), name="todo")
]
