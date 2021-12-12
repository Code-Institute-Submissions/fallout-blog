from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Categories(models.Model):
    """
    Model for creating categories
    """
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    A model for creating a table where posts will be written
    and what information the posts will require
    """

    class Status(models.Manager):
        """
        Class to filer status and show only published posts
        on webpage
        """
        def get_queryset(self):
            """
            Function for returning only published posts
            """
            return super().get_queryset().filter(status='published')

    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='posted')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name="Categories", default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    objects = models.Manager()
    new_status = Status()

    class Meta:
        """
        Magic Meta class for showing posts by newest first
        """
        ordering = ['-posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        For getting the url of each individual post that is clicked on
        """
        return reverse('blog:post_view', args=[self.slug])


class Comment(models.Model):
    """
    A model for allowing users to comment
    on other people's posts aswell as comment on
    posts themselves
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    content = models.TextField()
    status = models.BooleanField(default=True)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for showing comments byy date published
        """
        ordering = ("publish",)

    def __str__(self):
        return f"Comment by {self.name}"


