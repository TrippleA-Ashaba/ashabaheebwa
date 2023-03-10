from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic import ListView, TemplateView

from .forms import CommentForm, ContactForm
from .models import Post

# get the current year for use in footer
YEAR = timezone.now().year


def get_all_posts():
    return Post.objects.filter(status=1)


# =====================the home view======================
def home_view(request):

    # get published posts
    posts = get_all_posts()
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
    sidebar_posts = get_all_posts()
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


# ================================== All posts view ========================
def all_posts_view(request):
    all_posts = get_all_posts()
    paginator = Paginator(all_posts, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "blog/all_posts.html",
        {
            "year": YEAR,
            "posts": page_obj,
            "sidebar_posts": all_posts,
            "title": "all posts",
        },
    )


# ================================= Programming =========================
def prog_view(request):
    posts = Post.objects.filter(category="programming")
    paginator = Paginator(posts, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/prog.html",
        {
            "year": YEAR,
            "posts": page_obj,
            "sidebar_posts": get_all_posts,
            "title": "Programming",
        },
    )


def tut_view(request):
    posts = Post.objects.filter(category="tutorial")

    paginator = Paginator(posts, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "blog/tut.html",
        {
            "year": YEAR,
            "posts": page_obj,
            "sidebar_posts": get_all_posts,
            "title": "Tutorials",
        },
    )


# ===============================the About page============================
class AboutView(TemplateView):
    extra_context = {"year": YEAR, "title": "about"}
    template_name = "blog/about.html"


# =========================The contact page=========================
class ContactView(TemplateView):
    extra_context = {"year": YEAR, "title": "contact"}
    template_name = "blog/contact.html"


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Blog Contact: {form.cleaned_data['name']}, {form.cleaned_data['subject']}"
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email_from = form.cleaned_data["email"]
            email_to = "zaphod@gmail.com"

            html = render_to_string(
                "emails/contact_form.html",
                {
                    "name": name,
                    "email": email_from,
                    "subject": subject,
                    "message": message,
                    "head": "BLOG CONTACT",
                },
            )
            messages.success(request, "Email was sent Successfully!")

            send_mail(
                subject=subject,
                message=message,
                from_email=email_from,
                recipient_list=[email_to],
                html_message=html,
                fail_silently=False,
            )
            return redirect("blog_contact")

        else:
            messages.warning(request, "Something Wrong, Email was not sent!")

    return render(
        request, "blog/contact.html", {"year": YEAR, "title": "contact", "form": form}
    )


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
