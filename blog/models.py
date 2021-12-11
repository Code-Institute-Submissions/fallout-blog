from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
        return reverse('blog:post_view', args=[self.slug])

    
