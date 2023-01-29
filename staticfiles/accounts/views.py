from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# class AccountPasswordChangeView(PasswordChangeView):
#     template_name = "registration/password_change_form.html"
#     success_url = reverse_lazy("password_change_done")
