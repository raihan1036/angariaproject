# news/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    
    # FIX: Change 'image' to 'featured_image'
    fields = ['title', 'content', 'featured_image', 'published_date']
    
    list_display = ('title', 'image_thumbnail', 'published_date')
    search_fields = ('title', 'content')

    @admin.display(description="Image")
    def image_thumbnail(self, obj):
        # FIX: Check for 'obj.featured_image'
        if obj.featured_image and hasattr(obj.featured_image, 'url'):
            return format_html(f'<img src="{obj.featured_image.url}" style="height: 40px; width: auto;" />')
        return "No Image"

admin.site.register(BlogPost, BlogPostAdmin)