# -*- coding: utf-8 -*-

"""Console Script: Django First app Tutorial part 5

This is the script presented in part 5 of Django's first app tutorial,
source at:
https://docs.djangoproject.com/en/4.1/intro/tutorial05/

It deals with experimenting with django's unit testing functions in the
console before moving on to writing proper test unit's

NOTE: This is a django console script (i.e. it is meant to:
    1. Either be executed directly with pycharm's "run in python console"
    option enabled in this script's run configuration.
    2. Or to be imported into a new django console.
    3. Or to be executed with pycharm ExecuteInConsole Action
), in any case it requires django_manage_shell to have been activated.
"""
# --------------------
# IMPORTS
# --------------------
# Standard library imports:
from datetime import timedelta

# Django imports:
from django.utils import timezone
from django.urls import reverse
from django.test.utils import setup_test_environment
from django.test import Client

# Local imports:
from polls.models import Question

# --------------------
# CONSTANTS
# --------------------

# --------------------
# CLASSES
# --------------------

# --------------------
# FUNCTIONS
# --------------------


# --------------------
# DIRECT EXECUTION
# --------------------
setup_test_environment()

# == Before fixing the Question models' was_published_recently function.
# Create a question with the publication date of tomorrow.
question = Question(
    question_text="manual test 1",
    publication_date=timezone.now() + timedelta(days=1)
)
question.save()
# Check if the new question is reported as recent.
# Before the above-mentioned bug is fixed this will return True.
question.is_recent_publication()

# ... test is continued as a proper test in polls/tests.py

# ==test urls
client = Client()
# test response from "/"
response = client.get("/")
print(response.status_code)

# test response from "/polls/
response = client.get(reverse("polls:index"))
print(response, response.status_code, sep="\n")
print(response.content)
print([
    f"{key}: {value}"
    for key, value
    in response.context
], sep="\n")
print(response.context["questions_list"], sep="\n")
