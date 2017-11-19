from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import *
from comments.models import *
from core.models import *
from django.core.exceptions import PermissionDenied
# Create your views here.


class StartPage(ListView):
    template_name = "base.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(StartPage, self).get_context_data(**kwargs)
        context['Blogs'] = Blog.objects.order_by('-created_at')[0:10]
        context['Posts'] = Post.objects.order_by('-created_at')[0:10]
        context['title'] = 'Start page'
        context['user'] = self.request.user
        return context


class ProfileList(ListView):
    template_name = "profile_list.html"
    context_object_name = "Users"

    def get_context_data(self, **kwargs):
        context = super(ProfileList, self).get_context_data(**kwargs)
        context['title'] = 'Profiles'
        return context

    def get_queryset(self):
        queryset = User.objects.order_by('date_joined')
        return queryset


class ProfileMainDetail(DetailView):
    template_name = "profile_main_page.html"
    context_object_name = "user"
    model = User

    def get_context_data(self, **kwargs):
        context = super(ProfileMainDetail, self).get_context_data(**kwargs)
        context['title'] = 'Profile'
        context['you'] = self.request.user
        return context

    # def get_object(self):
    #     obj = super(ProfileMainDetail, self).get_object()
    #     if (obj.id != self.request.user.id):
    #         raise PermissionDenied
    #     return obj

