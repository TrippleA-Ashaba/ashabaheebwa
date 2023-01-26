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
    name = forms.CharField(
        max_length=80,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tim Berners-Lee",
            }
        ),
    )
    email = forms.EmailField(
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "placeholder": "i_invented@internet.com",
            }
        ),
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "The Hitchhiker's guide to the Internet",
            }
        ),
    )
    message = forms.CharField(
        widget=(
            forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Zaphod Beeblebrox is the key... I also love squirrels.",
                }
            )
        )
    )
