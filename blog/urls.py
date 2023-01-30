from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="blog_home"),
    path("about/", views.AboutView.as_view(), name="blog_about"),
    path("programming/", views.programmingView, name="blog_programming"),
    path("tutorials/", views.tutorialView, name="blog_tutorials"),
    path("contact/", views.contact, name="blog_contact"),
    path("search/", views.SearchView.as_view(), name="blog_search"),
    path("post/<slug:slug>/", views.post_detail_view, name="post_detail"),
]
