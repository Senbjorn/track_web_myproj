
from django.conf.urls import url
from blog.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^blog/categories/$', CategoryList.as_view(), name="category_list"),
    url(r'^blog/list/$', BlogList.as_view(), name="blog_list"),
    url(r'^blog/id(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^blog/create/$', login_required(CreateBlog.as_view()), name="blog_create"),
    url(r'^blog/id(?P<pk>\d+)/mypost/$', login_required(CreatePost.as_view()), name="post_create"),
    url(r'^blog/id(?P<pk>\d+)/edit/$', BlogDetail.as_view(), name="blog_edit"),
    url(r'^post/list/$', PostList.as_view(), name="post_list"),
    url(r'^post/id(?P<pk>\d+)/$', PostDetail.as_view(), name="post_detail"),
]
