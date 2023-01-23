from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'views', 'published_at', 'status')
    list_filter = ('status', 'created_at', 'published_at', 'author', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_at'
    readonly_fields = ('created_at', 'updated_at', 'views')
    ordering = ['status', 'published_at', 'views']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_title = 'Управление статьями блога'
admin.site.site_header = 'Управление статьями блога'
