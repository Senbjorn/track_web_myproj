from django.shortcuts import render
from django.shortcuts import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django import forms
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
    context_object_name = "cuser"
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


class ProfileCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ProfileCreate(CreateView):
    template_name = "signup.html"
    form_class = ProfileCreationForm

    def get_success_url(self):
        login(self.request, self.object)
        return reverse("core:startpage")