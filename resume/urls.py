from django.urls import path

from . import views

urlpatterns = [path("resume/", views.HomeView.as_view(), name="resume")]
