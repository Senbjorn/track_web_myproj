from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from comments.models import *


class CommentDetail(DetailView):
    template_name = "comment_detail.html"
    context_object_name = "idcom"
    model = Comment

    def get_context_data(self, **kwargs):
        context = super(CommentDetail, self).get_context_data(**kwargs)
        context['title'] = "Comment details"
        return context
