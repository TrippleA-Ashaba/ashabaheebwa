from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


# Create your models here.
class Post(models.Model):

    CATEGORY = (("programming", "programming"), ("tutorial", "tutorial"))
    STATUS = ((0, "draft"), (1, "published"))

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=True,
    )
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    category = models.CharField(max_length=15, choices=CATEGORY, default="tutorial")
    status = models.IntegerField(choices=STATUS, default=0)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_updated",)

    def __str__(self) -> str:
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    comment_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_published",)

    def __str__(self) -> str:
        return f"Comment {self.content} by {self.author}"
