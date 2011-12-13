from django.contrib import admin
from django.conf import settings

from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    model = Post
    
admin.site.register(Post, PostAdmin)