from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from datetime import date
from django.shortcuts import render
from .models import Post




def get_date(post):
    return post['date']
# Create your views here.

def index(request):

    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html",{
        "posts": latest_posts
    })


def get_posts_list(request):

    all_posts = Post.objects.all().order_by("-date")

    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def get_post(request, post_id):

    post = Post.objects.get(id=post_id)

    return render(request, "blog/post-detail.html", {
        "post" : post,
        "post_tags": post.tags.all()
    })