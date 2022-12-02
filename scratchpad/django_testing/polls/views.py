from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(
        '<p>This is the polls app index page.</p>'
        '<p><a href="..">Back to root index</a></p>'
    )
