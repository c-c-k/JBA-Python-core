from django import forms
from django.forms import ModelForm

from .models import PostcardModel, TITLE_CHOICES


class PostcardCustomForm(forms.Form):
    address = forms.CharField(label="Destination_address")
    author = forms.CharField(min_length=3)
    compliment = forms.CharField(max_length=1024)
    usage = forms.Select(choices=TITLE_CHOICES)
    delivery_date = forms.DateField(input_formats="%Y/%m/%d")
    email = forms.EmailField()


class PostcardModelForm(ModelForm):
    class Meta:
        labels = {"address": "Destination address"}
        model = PostcardModel
        fields = "__all__"


class PostcardModelFormDateAddressOnly(ModelForm):
    class Meta:
        model = PostcardModel
        fields = ['delivery_date', 'address']


class PostcardModelFormNoDate(ModelForm):
    class Meta:
        model = PostcardModel
        exclude = ['delivery_date']
