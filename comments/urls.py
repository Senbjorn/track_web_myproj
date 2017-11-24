from comments.views import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^id(?P<pk>\d+)/$', CommentDetail.as_view(), name="comment_detail"),
    url(r'^post_id(?P<pk>\d+)/create$', login_required(CreateComment.as_view()), name="comment_create"),
    url(r'^id(?P<pk>\d+)/edit/$', UpdateComment.as_view(), name="comment_update"),
]
