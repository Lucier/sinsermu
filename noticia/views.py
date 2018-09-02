# coding=utf-8

from watson import search as watson

from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Post


class PostListView(generic.ListView):

    template_name = 'noticia/noticia_list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset


noticia_list = PostListView.as_view()

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }

    return render(request, 'noticia/noticia.html', context)
