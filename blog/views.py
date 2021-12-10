from django.shortcuts import render
from .models import Post


def HomeView(request):
    posts = Post.new_status.all()

    return render(request, 'index.html', {'posts': posts})
