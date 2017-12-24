from django.contrib.auth.mixins import UserPassesTestMixin
from django import forms
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from blog.models import *
from comments.views import CommentListForm, comment_form_filter
from comments.models import Comment
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse as reverse_url
from django.contrib.contenttypes.fields import GenericRelation as GR


def blog_form_filter(my_form, query):
    if my_form.is_valid():
        if my_form.cleaned_data['order_by']:
            if my_form.cleaned_data['direction']:
                if my_form.cleaned_data['direction'] == 'asc':
                    query = query.order_by(my_form.cleaned_data['order_by'])
                elif my_form.cleaned_data['direction'] == 'desc':
                    query = query.order_by('-{}'.format(my_form.cleaned_data['order_by']))
            else:
                query = query.order_by(my_form.cleaned_data['order_by'])
        if my_form.cleaned_data['search']:
            query = query.filter(name=my_form.cleaned_data['search'])
    return query


def post_form_filter(my_form, query):
    if my_form.is_valid():
        if my_form.cleaned_data['order_by']:
            if my_form.cleaned_data['direction']:
                if my_form.cleaned_data['direction'] == 'asc':
                    query = query.order_by(my_form.cleaned_data['order_by'])
                elif my_form.cleaned_data['direction'] == 'desc':
                    query = query.order_by('-{}'.format(my_form.cleaned_data['order_by']))
            else:
                query = query.order_by(my_form.cleaned_data['order_by'])
        if my_form.cleaned_data['search']:
            query = query.filter(name=my_form.cleaned_data['search'])
    return query


class CategoryListForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('name', 'name'),
            ('id', 'id')
        ),
        required=False,
        label='sort by'
    )
    direction = forms.ChoiceField(
        choices=(
            ('inc', 'increase'),
            ('dec', 'decrease')
        ),
        required=False,
        label='order'
    )
    search = forms.CharField(required=False)


class BlogListForm(forms.Form):
    search = forms.CharField(required=False, label="Name")
    order_by = forms.ChoiceField(
        choices=(
            ('name', 'name'),
            ('created_at', 'date of creation'),
            ('updated_at', 'last update'),
        ),
        initial='name',
        required=False,
        label='Sort by',
    )
    direction = forms.ChoiceField(
        choices=(
            ('asc', 'asc'),
            ('desc', 'desc')
        ),
        initial='asc',
        required=False,
        label='Order'
    )


class PostListForm(forms.Form):
    search = forms.CharField(required=False, label="Name")
    order_by = forms.ChoiceField(
        choices=(
            ('name', 'name'),
            ('created_at', 'date of creation'),
            ('updated_at', 'last update'),
        ),
        initial='name',
        required=False,
        label='Sort by',
        # widget=forms.RadioSelect,
    )
    direction = forms.ChoiceField(
        choices=[
            ('asc', 'asc'),
            ('desc', 'desc'),
        ],
        initial='asc',
        required=False,
        label='Order',
        # widget=forms.RadioSelect,
    )


class BlogList(ListView):
    template_name = "blog/list_blogs.html"
    context_object_name = "blogList"
    model = Blog
    paginate_by = 10
    paginate_orphans = 2
    my_form = None

    def dispatch(self, request, *args, **kwargs):
        self.my_form = BlogListForm(self.request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['title'] = "Blog list"
        context['form'] = self.my_form
        context['heading'] = "Blogs"
        return context

    def get_queryset(self):
        query = super(BlogList, self).get_queryset()
        return blog_form_filter(self.my_form, query)


class BlogDetail(ListView):
    template_name = "blog/detail_blog.html"
    context_object_name = "posts"
    model = Post
    paginate_by = 10
    paginate_orphans = 2
    my_blog = None
    my_form = None

    def dispatch(self, request, *args, **kwargs):
        self.my_blog = get_object_or_404(Blog.objects.all(), id=kwargs['pk'])
        self.my_form = PostListForm(self.request.GET)
        return super(BlogDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['title'] = self.my_blog.name
        context['idblog'] = self.my_blog
        context['form'] = self.my_form
        context['heading'] = self.my_blog.name
        return context

    def get_queryset(self):
        query = super(BlogDetail, self).get_queryset()
        query = query.filter(blog=self.my_blog)
        return post_form_filter(self.my_form, query)


class PostList(ListView):
    template_name = "post_list.html"
    context_object_name = "postList"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['title'] = "Post list"
        return context


class PostDetail(ListView):
    template_name = "blog/detail_post.html"
    context_object_name = "comments"
    model = Comment
    paginate_by = 10
    paginate_orphans = 2
    my_form = None
    my_post = None

    def dispatch(self, request, *args, **kwargs):
        self.my_form = CommentListForm(self.request.GET)
        self.my_post = get_object_or_404(Post.objects.all(), id=kwargs['pk'])
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['title'] = self.my_post.name
        context['idpost'] = self.my_post
        context['form'] = self.my_form
        context['heading'] = self.my_post.name
        return context

    def get_queryset(self):
        query = super(PostDetail, self).get_queryset()
        query = query.filter(post=self.my_post)
        return comment_form_filter(self.my_form, query)


class CreateBlog(CreateView):
    template_name = "blog/action_create_blog.html"
    model = Blog
    fields = 'categories', 'name', 'description'
    success_url = ""

    def form_valid(self, form):
        form.instance.owner = self.request.user
        super(CreateBlog, self).form_valid(form)
        return HttpResponse("OK");

    def get_success_url(self):
        return self.success_url


class UpdateBlog(UserPassesTestMixin, UpdateView):
    template_name = "blog/action_update_blog.html"
    model = Blog
    fields = 'description',
    context_object_name = 'blog'
    success_url = ""

    raise_exception = True

    def test_func(self):
        return self.get_object().owner == self.request.user

    def form_valid(self, form):
        super(UpdateBlog, self).form_valid(form)
        return HttpResponse("OK")

    def get_success_url(self):
        return self.success_url


class UpdatePost(UserPassesTestMixin, UpdateView):
    template_name = "blog/action_update_post.html"
    model = Post
    fields = 'text',
    context_object_name = "post"
    success_url = ""

    raise_exception = True

    def test_func(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        super(UpdatePost, self).form_valid(form)
        from django.http import HttpResponse
        return HttpResponse("OK")

    def get_success_url(self):
        return self.success_url


class CreatePost(UserPassesTestMixin, CreateView):
    template_name = "blog/action_create_post.html"
    model = Post
    fields = 'text', 'name'
    raise_exception = True
    my_blog = None
    success_url = ""

    def test_func(self):
        return self.my_blog.owner == self.request.user

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['blog'] = self.my_blog
        return context

    def dispatch(self, request, *args, **kwargs):
        self.my_blog = get_object_or_404(Blog.objects.all(), id=self.kwargs['pk'])
        # if self.my_blog.owner != self.request.user:
        #     return redirect(reverse_url("blog:post_creation_denied", kwargs={'pk': self.my_blog.id}))
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.my_blog
        super(CreatePost, self).form_valid(form)
        return HttpResponse("OK")

    def get_success_url(self):
        return self.success_url

class CategoryList(ListView):
    template_name = "category_list.html"
    context_object_name = "categoryList"
    model = Category
    my_form = None

    def dispatch(self, request, *args, **kwargs):
        self.my_form = CategoryListForm(self.request.GET)
        return super(CategoryList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['title'] = "Category list"
        context['form'] = self.my_form
        return context

    def get_queryset(self):
        query = super(CategoryList, self).get_queryset()
        if self.my_form.is_valid():
            if self.my_form.cleaned_data['order_by']:
                if self.my_form.cleaned_data['direction']:
                    if self.my_form.cleaned_data['direction'] == 'inc':
                        query = query.order_by(self.my_form.cleaned_data['order_by'])
                    elif self.my_form.cleaned_data['direction'] == 'dec':
                        query = query.order_by('-{}'.format(self.my_form.cleaned_data['order_by']))
                else:
                    query = query.order_by(self.my_form.cleaned_data['order_by'])
            if self.my_form.cleaned_data['search']:
                query = query.filter(name=self.my_form.cleaned_data['search'])
        return query


class PostCommentsList(ListView):
    template_name = "post_comments_list.html"
    model = Comment
    context_object_name = "comments"

    def get_queryset(self):
        query = super(PostCommentsList, self).get_queryset()
        post = get_object_or_404(Post.objects.all(), id=self.kwargs['pk'])
        query.filter(post=post)
        return query