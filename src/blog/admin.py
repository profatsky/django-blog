from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'published_at', 'status')
    list_filter = ('status', 'created_at', 'published_at', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_at'
    readonly_fields = ('created_at', 'updated_at',)
    ordering = ['status', 'published_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


admin.site.site_title = 'Управление статьями блога'
admin.site.site_header = 'Управление статьями блога'
