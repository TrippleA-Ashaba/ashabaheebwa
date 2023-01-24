from django import forms
from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    author = forms.CharField(
        label="Name",
        min_length=5,
        widget=forms.TextInput(attrs={"placeholder": "Enter Name"}),
    )

    class Meta:
        model = Comment
        fields = ("author", "email", "content")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80, min_length=5)
    email = forms.EmailField(max_length=80)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=(forms.Textarea(attrs={"rows": 4})))
