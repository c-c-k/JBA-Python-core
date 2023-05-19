from django.shortcuts import render, HttpResponse, Http404
from django.views import View

from . import models


# Create your views here.
class CandyFactoryIndex(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, "candy_factory/index.html",
            context={
                "candies": models.CANDIES,
            }
        )


class CandyInfo(View):
    def get(self, request, candy_name, *args, **kwargs):
        try:
            candy_info = models.CANDIES[candy_name]
        except KeyError as err:
            raise Http404().with_traceback(err.__traceback__)
            # return HttpResponse(status=404)
        return render(
            request, "candy_factory/candy_info.html",
            context={
                "candy_name": candy_name,
                "candy_info": candy_info,
            }
        )
