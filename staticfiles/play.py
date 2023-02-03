from blog.models import Post
from blog.views import get_all_posts


all_posts = get_all_posts()
# posts = [post for post in all_posts if post.category == "tutorial"]


print(all_posts)
