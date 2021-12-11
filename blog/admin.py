from django.contrib import admin
from . import models


@admin.register(models.Post)
class AdminView(admin.ModelAdmin):
    """
    Displaying the posts within the admin section of the site
    """
    list_display = ('title', 'slug', 'author', 'status',)
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Comment)
class CommentView(admin.ModelAdmin):
    """
    Displaying the comments within the admin section of the site
    """
    list_display = ('post', 'name', 'publish', 'status',)
    list_filter = ('status', 'publish')
    search_fields = ('name', 'content',)
