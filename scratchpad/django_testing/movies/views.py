from django.shortcuts import render

# placeholder model access.
from .models import DIRECTOR, MOVIES


# Create your views here.
def movies(request):
    return render(
        request=request, template_name='movies/movies.html',
        context={
            'director': DIRECTOR,
            'movies': MOVIES,
        },
    )
