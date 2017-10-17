from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from blog.models import *

# Create your views here.

class BlogList(ListView):
    template_name = "blog_list.html"
    context_object_name = "blogList"
    # queryset = Blog.objects.all()
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['title'] = "Blog list"
        return context


class BlogDetail(DetailView):
    template_name = "blog_detail.html"
    context_object_name = "idblog"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['title'] = "Blog details"
        return context


class PostList(ListView):
    template_name = "post_list.html"
    context_object_name = "postList"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['title'] = "Post list"
        return context


class PostDetail(DetailView):
    template_name = "post_detail.html"
    context_object_name = "idpost"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['title'] = "Post details"
        return context
# def blog_list(request):
#     return render(request, "blog_list.html", {'title': 'Blog list'})