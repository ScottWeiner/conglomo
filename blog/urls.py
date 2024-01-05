from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("posts", views.get_posts_list, name="posts-list"), 
    path("posts/<post_id>", views.get_post, name="post-detail") 
]