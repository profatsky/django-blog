from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail')
]
