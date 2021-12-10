from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A model for creating a table where posts will be written
    and what information the posts will require
    """

    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    posted_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
