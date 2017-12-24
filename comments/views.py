from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django import forms
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from comments.models import *


def comment_form_filter(my_form, query):
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
            query = query.filter(author__username=my_form.cleaned_data['search'])
    return query


class CommentListForm(forms.Form):
    search = forms.CharField(required=False, label='Author')
    order_by = forms.ChoiceField(
        choices=(
            ('author', 'author'),
            ('created_at', 'date')
        ),
        required=False,
        label='sort by',
        # widget=forms.RadioSelect
    )
    direction = forms.ChoiceField(
        choices=(
            ('asc', 'asc'),
            ('desc', 'desc')
        ),
        required=False,
        label='order',
        # widget=forms.RadioSelect
    )


class CommentDetail(DetailView):
    template_name = "comment_detail.html"
    context_object_name = "idcom"
    model = Comment

    def get_context_data(self, **kwargs):
        context = super(CommentDetail, self).get_context_data(**kwargs)
        context['title'] = "Comment details"
        return context


class CreateComment(CreateView):
    template_name = "comment_create.html"
    context_object_name = "comment"
    model = Comment
    fields = "text",
    my_post = None

    def dispatch(self, request, *args, **kwargs):
        self.my_post = get_object_or_404(Post, id = kwargs['pk'])
        return super(CreateComment, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.my_post
        return super(CreateComment, self).form_valid(form)

    def get_success_url(self):
        return reverse("comments:comment_detail", kwargs={'pk': self.object.id})


class UpdateComment(UserPassesTestMixin, UpdateView):
    template_name = "comment_update.html"
    context_object_name = "comment"
    model = Comment
    fields = "text",
    raise_exception = True
    success_url = ""

    def test_func(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        super(UpdateComment, self).form_valid(form)
        from django.http import HttpResponse
        return HttpResponse("OK");

    def get_success_url(self):
        return self.success_url;


