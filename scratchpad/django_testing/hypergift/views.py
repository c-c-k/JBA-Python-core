from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import PostcardModelForm

def index_view(request):
    return render(request, "hypergift/index.html")


class PostcardFormView(FormView):
    form_class = PostcardModelForm
    template_name = "hypergift/model_form.html"
    success_url = reverse_lazy("hypergift:index")



