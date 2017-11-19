from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.
from like.models import LikeDislike


class LikeDetail(DetailView):
    model = LikeDislike
    template_name = "like_Detail.py.html"
    context_object_name = "like"

    def get_context_data(self, **kwargs):
        context = super(LikeDislike, self).get_context_data(**kwargs)
        context['title'] = "Like #{}".format(self.object.id)


class LikeList(ListView):
    model = LikeDislike
    template_name = "like_list.html"
    context_object_name = ""

    def get_context_data(self, **kwargs):
        context = super(LikeDislike, self).get_context_data(**kwargs)
        context['title'] = "Like list"
