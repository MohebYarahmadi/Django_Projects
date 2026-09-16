from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published_at', 'status']
    list_filter = ['status', 'author', 'created_at', 'published_at']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published_at'
    ordering = ['-published_at', 'status']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'is_verified', 'created_at']
    list_filter = ['is_verified', 'created_at', 'updated_at']
    search_fields = ['name', 'email', 'body']
