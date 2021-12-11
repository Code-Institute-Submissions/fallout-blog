from django.shortcuts import render, get_object_or_404
from .models import Post


def HomeView(request):
    """
    A view for the homepage
    """
    posts = Post.new_status.all()

    return render(request, 'index.html', {'posts': posts})


def Post_View(request, post):
    """
    A view for looking at the details of a blog post
    """
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_detail.html', {'post': post})