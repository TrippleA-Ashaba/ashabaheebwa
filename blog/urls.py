from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="blog_home"),
    path("post/<slug:slug>/", views.post_detail_view, name="post_detail"),
    path("about/", views.AboutView.as_view(), name="blog_about"),
    path("programming/", views.ProgrammingView.as_view(), name="blog_chats"),
    path("tutorials/", views.TutorialView.as_view(), name="blog_tutorials"),
    path("contact/", views.ContactView.as_view(), name="blog_contact"),
    path("search/", views.SearchView.as_view(), name="blog_search"),
]
