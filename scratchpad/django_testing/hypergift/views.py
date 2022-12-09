from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import PostcardModelForm, PostcardCustomForm
from .models import PostcardModel


def index_view(request):
    return render(request, "hypergift/index.html")


class PostcardCustomFormView(View):
    form_class = PostcardCustomForm
    form_template = "hypergift/custom_form.html"

    def get(self, request, *args, **kwargs):
        postcard_form = self.form_class()
        context = {"form": postcard_form}
        return render(request, self.form_template, context)

    def post(self, request, *args, **kwargs):
        postcard_form = self.form_class(request.POST)
        is_valid_form = postcard_form.is_valid()
        cleaned_data =postcard_form.cleaned_data
        if is_valid_form:
            new_postcard = self.form_class()
            clean_form = self.form_class()
            context = {"form": clean_form}
        else:
            if "delivery_date" not in cleaned_data:
                postcard_form.add_error(
                    "delivery_date",
                    "Please enter date in the format YYYY/MM/DD"
                )
            if "email" not in cleaned_data:
                postcard_form.add_error(
                    "email",
                    "Please add a proper email address (user@provider.domain)"
                )
            context = {"form": postcard_form}
        return render(request, self.form_template, context)



class PostcardModelFormView(FormView):
    form_class = PostcardModelForm
    template_name = "hypergift/model_form.html"
    success_url = reverse_lazy("hypergift:index")
