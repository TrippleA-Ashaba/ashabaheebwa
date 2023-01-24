from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import ListView, TemplateView

from .forms import CommentForm
from .models import Post

# get the current year for use in footer
YEAR = timezone.now().year


# =====================the home view======================
def home_view(request):

    # get published posts
    posts = Post.objects.filter(status=1)
    programming_posts = posts.filter(category="programming")
    tutorial_posts = posts.filter(category="tutorial")

    return render(
        request,
        "blog/home.html",
        {
            "title": "home",
            "year": YEAR,
            "posts": posts,
            "programming_posts": programming_posts,
            "tutorial_posts": tutorial_posts,
        },
    )


# ============================single post view================================
def post_detail_view(request, slug):
    # get post by slug name instead of postID
    post = Post.objects.get(slug=slug)
    # print(post.id)
    sidebar_posts = Post.objects.filter(status=1)
    comments = post.comments.filter(comment_post=post)

    # time for use on timesince in comment section
    today = timezone.now()

    # Comment form
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = post
            comment.save()
            messages.success(request, "Comment Saved Successfully!")
            return redirect(
                "post_detail",
                slug=post.slug,
            )
        else:
            messages.warning(request, "Something Wrong, Comment was not saved!")

    else:
        form = CommentForm()

    return render(
        request,
        "blog/post.html",
        {
            "post": post,
            "sidebar_posts": sidebar_posts,
            "year": YEAR,
            "title": post.title[:20],
            "comments": comments,
            "today": today,
            "form": form,
        },
    )


# =======================Get tutorial posts only===========================
class TutorialView(ListView):
    model = Post
    posts = Post.objects.filter(status=1, category="tutorial")
    sidebar_posts = Post.objects.filter(status=1)

    extra_context = {
        "year": YEAR,
        "posts": posts,
        "sidebar_posts": sidebar_posts,
        "category": "tutorials",
        "title": "tutorials",
    }
    template_name = "blog/category.html"


# ============================Get chat posts================================
class ProgrammingView(ListView):
    model = Post
    posts = Post.objects.filter(status=1, category="programming")
    sidebar_posts = Post.objects.filter(status=1)

    extra_context = {
        "year": YEAR,
        "posts": posts,
        "sidebar_posts": sidebar_posts,
        "category": "programming",
        "title": "programmming",
    }
    template_name = "blog/category.html"


# ===============================the About page============================
class AboutView(TemplateView):
    extra_context = {"year": YEAR, "title": "about"}
    template_name = "blog/about.html"


# =========================The contact page=========================
class ContactView(TemplateView):
    extra_context = {"year": YEAR, "title": "contact"}
    template_name = "blog/contact.html"


# ============================ Show posts matching user search===========================
class SearchView(ListView):
    model = Post

    sidebar_posts = Post.objects.filter(status=1)

    extra_context = {
        "year": YEAR,
        "sidebar_posts": sidebar_posts,
        "title": "search",
    }

    template_name = "blog/search-result.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
        return post_list
