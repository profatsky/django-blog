from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from .models import Post, Category


def index(request):
    return redirect('post_list')


class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published')


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'

    def get_object(self, **kwargs):
        post = Post.objects.get(slug=self.kwargs['post_slug'], status='published')
        if not post:
            raise Http404
        post.views += 1
        post.save()
        return post


class PostListByCategory(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['category_slug'], status='published'
        ).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = Category.objects.get(slug=self.kwargs['category_slug'])
        return context
