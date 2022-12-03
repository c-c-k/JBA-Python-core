from datetime import timedelta
from django.db import models
from django.utils import timezone
from random import randint, sample


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return (
            self.publication_date
            >= timezone.now() - timedelta(days=1)
        )

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote_tally = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


def create_questions() -> list[Question]:
    return [
        Question(
            question_text=f"Ipsum lorem #{num}",
            publication_date=timezone.now() - timedelta(days=-1 * num)
        )
        for num
        in sample(range(1, 100), k=5)
    ]


def create_choices(questions: list[Question]) -> list[Choice]:
    return [
        Choice(
            question=question,
            choice_text=f"Ipsum lorem --{num}--",
            vote_tally=randint(0, 20)
        )
        for num
        in range(1, 5)
        for question
        in questions
    ]


def populate_db():
    for model in (Question, Choice):
        model.objects.all().delete()
    questions = create_questions()
    choices = create_choices(questions)
    model_objects: list[models.Model] = [*questions, *choices]
    for model_object in model_objects:
        model_object.save()
