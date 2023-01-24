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
