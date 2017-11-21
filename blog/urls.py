
from django.conf.urls import url
from blog.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^categories/$', CategoryList.as_view(), name="category_list"),
    url(r'^list/$', BlogList.as_view(), name="blog_list"),
    url(r'^id(?P<pk>\d+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^create/$', login_required(CreateBlog.as_view()), name="blog_create"),
    url(r'^id(?P<pk>\d+)/post/$', CreatePost.as_view(), name="post_create"),
    url(r'^id(?P<pk>\d+)/edit/$', UpdateBlog.as_view(), name="blog_edit"),
    url(r'^post/list/$', PostList.as_view(), name="post_list"),
    url(r'^post/id(?P<pk>\d+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'^post/id(?P<pk>\d+)/edit/$', UpdatePost.as_view(), name="post_update"),
]
