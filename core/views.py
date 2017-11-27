from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from blog.models import *
from comments.models import *
from core.models import *
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


class ProfileDataList(ListView):
    my_user = None

    def dispatch(self, request, *args, **kwargs):
        self.my_user = get_object_or_404(User.objects.all(), id=kwargs['pk'])
        return super(ProfileDataList, self).dispatch(request, *args, **kwargs)


class ProfileBlogList(ProfileDataList):
    template_name = "profile_blogs.html"
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super(ProfileBlogList, self).get_queryset()
        return queryset.filter(owner=self.my_user)


class ProfilePostList(ProfileDataList):
    template_name = "profile_posts.html"
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return super(ProfilePostList, self).get_queryset().filter(author=self.my_user)


class ProfileCommentList(ProfileDataList):
    template_name = "profile_comments.html"
    model = Comment
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = super(ProfileCommentList, self).get_queryset()
        return queryset.filter(author=self.my_user)


class ProfileFavoriteList(ProfileDataList):
    template_name = "profile_favorites.html"
    context_object_name = 'list'
    model = LikeDislike

    def get_queryset(self):
        return super(ProfileFavoriteList, self).get_queryset().filter(user=self.my_user)


class ProfileDataForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileCreationForm(UserCreationForm, ProfileDataForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ProfileCreate(CreateView):
    template_name = "signup.html"
    form_class = ProfileCreationForm

    def get_success_url(self):
        login(self.request, self.object)
        return reverse("core:startpage")


class ProfileUpdate(UpdateView):
    template_name = "profile_update.html"
    form_class = ProfileDataForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("core:profile_main_page", kwargs={'pk': self.request.user.id})


class ProfileUpdatePass(UpdateView):
    template_name = "profile_update.html"
    form_class = PasswordChangeForm

    def get_form(self, form_class=None):
        return self.form_class(self.request.user, self.request.POST)

    def dispatch(self, request, *args, **kwargs):
        kwargs['user'] = self.request.user
        return super(ProfileUpdatePass, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        login(self.request, get_object_or_404(User.objects.all(), id=self.request.user.id))
        return reverse("core:profile_main_page", kwargs={'pk': self.request.user.id})