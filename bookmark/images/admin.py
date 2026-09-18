from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'slug', 'created_at']
    list_filter = ['created_at']
