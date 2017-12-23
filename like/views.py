from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django import forms
from django.http import HttpResponse
# Create your views here.
from like.models import LikeDislike
from core.models import User
from blog.models import Post
from comments.models import Comment


class LikeButtonForm(forms.Form):
    user_id = forms.IntegerField(required=True)
    object_id = forms.IntegerField(required=True)
    content_type = forms.CharField(required=True)


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


@login_required
def like_something(request):
    # try:
    if request.method == "POST":
        form = LikeButtonForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["user_id"]
            content_type = form.cleaned_data['content_type']
            object_id = form.cleaned_data['object_id']
            user = User.objects.all().get(id=user_id)
            if content_type == "Post":
                obj = Post.objects.all().get(id=object_id)
            if content_type == "Comment":
                obj = Comment.objects.all().get(id=object_id)
            if not obj.likes.filter(user=user):
                obj.likes.create(user=user)
                # LikeDislike.objects.create(user=user, content_object=obj)
                return HttpResponse("OK")
    # except:
    #     pass
    return HttpResponse("ERROR")