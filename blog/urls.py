from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="blog_home"),
    path("about/", views.AboutView.as_view(), name="blog_about"),
    path("all-posts/", views.all_posts_view, name="all_posts"),
    path("progs/", views.prog_view, name="blog_prog"),
    path("contact/", views.contact, name="blog_contact"),
    path("search/", views.SearchView.as_view(), name="blog_search"),
    path("post/<slug:slug>/", views.post_detail_view, name="post_detail"),
]
