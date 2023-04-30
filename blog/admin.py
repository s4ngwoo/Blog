from django.contrib import admin
from .models import Post, PostCategory, PostSeries, PostTag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'branch', 'language', 'created_at')
    list_filter = ('branch', 'id')
    search_fields = ['title', 'content']

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']

    pass

class PostSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']
    pass

class PostTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(PostSeries, PostSeriesAdmin)
admin.site.register(PostTag, PostTagAdmin)
