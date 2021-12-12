from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Categories
from .forms import CommentForm
from django.views.generic import ListView


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
    comments = post.comments.filter(status=True)
    user_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, })


class CategoryView(ListView):
    """
    A view for displaying posts by their categories
    """
    template_name = 'categories.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


def CategoryListView(request):
    CategoryListView = Categories.objects.all()
    context = {
        'CategoryListView': CategoryListView,
    }
    return context

