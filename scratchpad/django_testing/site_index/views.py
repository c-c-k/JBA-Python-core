from django.conf import settings
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(
        request=request,
        template_name='site_index/index.html',
        context={'applications': settings.APPLICATION_URLS},


    )
