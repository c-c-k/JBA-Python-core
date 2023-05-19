from django.shortcuts import redirect, HttpResponse
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        task = request.POST["todo"]
        important = request.POST["important"]
        todo_list = self.all_todos
        if task and task not in todo_list:
            if important:
                todo_list.insert(0, task)
            else:
                todo_list.append(task)
        return redirect("/")
