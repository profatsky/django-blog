from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail

from .models import Post, Category
from mailings.models import Subscriber


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

    def save_model(self, request, obj, form, change):
        if (not change or 'status' in form.changed_data) and obj.status == 'published':
            for subscriber in Subscriber.objects.all():
                send_mail(
                    subject='Блог',
                    message=f'{subscriber.name}, в Блоге вышла новая статья «{obj.title}» '
                            f'из категории «{obj.category.title}»!',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[subscriber.email]
                )
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_title = 'Управление статьями блога'
admin.site.site_header = 'Управление статьями блога'
