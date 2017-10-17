
from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^blog/list/$', BlogList.as_view(), name="blog_list"),
    url(r'^blog/id(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^post/list/$', PostList.as_view(), name="post_list"),
    url(r'^post/id(?P<pk>\d+)/$', PostDetail.as_view(), name="post_detail"),
]