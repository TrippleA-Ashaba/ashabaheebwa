from django.urls import path

from . import views

urlpatterns = [
    path("programming/", views.ProgrammingView.as_view(), name="blog_chats"),
    path("tutorials/", views.TutorialView.as_view(), name="blog_tutorials"),
    path("", views.home_view, name="blog_home"),
    path("about/", views.AboutView.as_view(), name="blog_about"),
    path("contact/", views.contact, name="blog_contact"),
    path("search/", views.SearchView.as_view(), name="blog_search"),
    path("post/<slug:slug>/", views.post_detail_view, name="post_detail"),
]
