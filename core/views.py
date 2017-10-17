from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import *
from comments.models import *
# Create your views here.


class StartPage(ListView):
    template_name = "base.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(StartPage, self).get_context_data(**kwargs)
        context['Blogs'] = Blog.objects.order_by('created_at')[0:10]
        context['Posts'] = Post.objects.order_by('created_at')[0:10]
        context['title'] = 'Start page'
        return context
