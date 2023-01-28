from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<slug:post_slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('categories/<slug:category_slug>/', views.PostListByCategory.as_view(), name='post_list_by_category')
]
