from django.contrib.contenttypes.models import ContentType
from django import forms
from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from blog.models import *
from django.contrib.contenttypes.fields import GenericRelation as GR

# Create your views here.


class CategoryListForm(forms.Form):
    order_by = forms.ChoiceField(choices=(
            ('name', 'name'),
            ('id', 'id')
        ),
        required=False,
        label='sort by'
    )
    direction = forms.ChoiceField(choices=(
        ('+' , 'increase'),
        ('-' , 'decrease')
        ),
        required=False,
        label='order'
    )
    search = forms.CharField(required=False)


class BlogListForm(forms.Form):
    order_by = forms.ChoiceField(choices=(
        ('name', 'name'),
        ('id', 'id'),
        ('created_at', 'date of creation')
        ),
        required=False,
        label='sort by'
    )
    direction = forms.ChoiceField(choices=(
        ('+', 'increase'),
        ('-', 'decrease')
        ),
        required=False,
        label='order'
    )
    search = forms.CharField(required=False);

class PostListForm(forms.Form):
    order_by = forms.ChoiceField(choices=(
        ('name', 'name'),
        ('id', 'id'),
        ('created_at', 'date of creation')
    ),
        required=False,
        label='sort by'
    )
    direction = forms.ChoiceField(choices=(
        ('+', 'increase'),
        ('-', 'decrease')
    ),
        required=False,
        label='order'
    )
    search = forms.CharField(required=False);

class BlogList(ListView):
    template_name = "blog_list.html"
    context_object_name = "blogList"
    # queryset = Blog.objects.all()
    model = Blog
    my_form = None

    def dispatch(self, request, *args, **kwargs):
        self.my_form = BlogListForm(self.request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['title'] = "Blog list"
        context['form'] = self.my_form
        return context

    def get_queryset(self):
        query = super(BlogList, self).get_queryset()
        if self.my_form.is_valid():
            if self.my_form.cleaned_data['order_by']:
                if self.my_form.cleaned_data['direction']:
                    if self.my_form.cleaned_data['direction'] == '+':
                        query = query.order_by(self.my_form.cleaned_data['order_by'])
                    elif self.my_form.cleaned_data['direction'] == '-':
                        query = query.order_by('-{}'.format(self.my_form.cleaned_data['order_by']))
                else:
                    query = query.order_by(self.my_form.cleaned_data['order_by'])
            if self.my_form.cleaned_data['search']:
                query = query.filter(name=self.my_form.cleaned_data['search'])
        return query


class BlogDetail(ListView):
    template_name = "blog_detail.html"
    context_object_name = "posts"
    model = Post
    my_blog = None
    my_form = None

    def dispatch(self, request, *args, **kwargs):
        self.my_blog = get_object_or_404(Blog.objects.all(), id=kwargs['pk'])
        self.my_form = BlogListForm(self.request.GET)
        return super(BlogDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['title'] = "Blog details"
        context['idblog'] = self.my_blog
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


class PostLikeList(DetailView):
    model = Post
    template_name = "post_like_list.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(PostLikeList, self).get_context_data(**kwargs)
        context['title'] = "Like list"
# def blog_list(request):
#     return render(request, "blog_list.html", {'title': 'Blog list'})


class CreateBlog(CreateView):
    template_name = "blog_create.html"
    model = Blog
    fields = 'categories', 'name', 'description'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateBlog, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})


class UpdateBlog(UpdateView):
    pass


class CreatePost(CreateView):
    template_name = "post_create.html"
    model = Post
    fields = 'text', 'name'
    my_blog = None

    def dispatch(self, request, *args, **kwargs):
        self.my_blog = get_object_or_404(Blog.objects.all(), id=kwargs['pk'])
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.my_blog
        return super(CreatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


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
                    if self.my_form.cleaned_data['direction'] == '+':
                        query = query.order_by(self.my_form.cleaned_data['order_by'])
                    elif self.my_form.cleaned_data['direction'] == '-':
                        query = query.order_by('-{}'.format(self.my_form.cleaned_data['order_by']))
                else:
                    query = query.order_by(self.my_form.cleaned_data['order_by'])
            if self.my_form.cleaned_data['search']:
                query = query.filter(name=self.my_form.cleaned_data['search'])
        return query