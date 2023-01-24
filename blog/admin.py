from django.contrib import admin

from .models import Comment, Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date_updated",
        "category",
        "status",
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "email",
        "content",
        "comment_post",
        "date_published",
    )
    list_filter = ("comment_post", "date_published")
    search_fields = ("author", "content")
