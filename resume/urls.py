from django.urls import path

from . import views

urlpatterns = [path("resume/", views.home, name="resume")]
