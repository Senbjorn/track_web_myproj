from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django import forms
from django.views.generic import DetailView
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
