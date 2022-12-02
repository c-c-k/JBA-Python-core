from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote_tally = models.IntegerField(default=0)
