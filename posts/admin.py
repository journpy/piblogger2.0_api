from .models import Post
from django.contrib import admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ModelAdmin for Post abject."""
    list_display = [
        'id', 'author', 'title', 'body', 'created_at', 'modified_at', 'slug'
        ]
    prepopulated_fields = {'slug':['title']} 
