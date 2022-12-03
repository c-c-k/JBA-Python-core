from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View

from . import models


class MainView(View):
    @staticmethod
    def reset_poll_data():
        models.populate_db()
        return redirect(".")

    @staticmethod
    def delete_choice(request):
        choice = models.Choice.objects.get(id=request.GET["choice_id"])
        choice.delete()
        return redirect(".")

    @staticmethod
    def delete_question(request):
        question = models.Question.objects.get(id=request.GET["question_id"])
        question.delete()
        return redirect(".")

    @staticmethod
    def present_index(request):
        questions = models.Question.objects.all()
        context = {
            "questions": questions
        }
        return render(request, "polls/index.html", context=context)

    def get(self, request, *args, **kwargs):
        if "reset_polls_data" in request.GET:
            response = self.reset_poll_data()
        elif "delete_choice" in request.GET:
            response = self.delete_choice(request)
        elif "delete_question" in request.GET:
            response = self.delete_question(request)
        else:
            response = self.present_index(request)
        return response
