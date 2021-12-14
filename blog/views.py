from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Categories
from .forms import CommentForm, PostForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def NewsPage(request):
    return render(request, 'news.html')


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
    all_comments = post.comments.filter(status=True)

    page = request.GET.get('page', 1)
    paginator = Paginator(all_comments, 6)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.number_pages)

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
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'all_comments': all_comments, })


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
    """
    A view for showing all of the cateogories 
    in the category list created in the admin section
    """
    CategoryListView = Categories.objects.all()
    context = {
        'CategoryListView': CategoryListView,
    }
    return context


def SearchView(request):
    """ A view for using the search bar in the navbar"""
    form = PostForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(title__contains=q)
    return render(request, 'nav_search.html', {'form': form, 'q': q, 'results': results, })


