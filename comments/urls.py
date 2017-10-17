from comments.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'comment/id(?P<pk>\d+)/$', CommentDetail.as_view(), name="comment_detail")
]