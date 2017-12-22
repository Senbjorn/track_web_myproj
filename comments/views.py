from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django import forms
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from comments.models import *


class CommentListForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('author', 'author'),
            ('id', 'id'),
            ('created_at', 'date')
        ),
        required=False,
        label='sort by'
    )
    direction = forms.ChoiceField(
        choices=(
            ('+', 'increase'),
            ('-', 'decrease')
        ),
        required=False,
        label='order'
    )
    search = forms.CharField(required=False, label='Author')


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


