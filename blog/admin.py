from django.contrib import admin
from . import models


class AdminView(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status',)


admin.site.register(models.Post, AdminView)
