from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_pk', 'status', 'language', 'created_on')
    list_filter = ('status', 'post_pk')
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
