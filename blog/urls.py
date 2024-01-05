from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #TODO: Create index() view
    path("posts", views.get_posts_list, name="posts-list"), #TODO: Cteate get_posts_list() view
    path("posts/<post_id>", views.get_post, name="post-detail") #TODO: Create get_post() view
]