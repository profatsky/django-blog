from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'

    def get_object(self, **kwargs):
        return get_object_or_404(Post, slug=self.kwargs.get('post_slug'), status='published')
