
from django.conf.urls import url
from core.views import *

urlpatterns = [
    url(r'^startpage/$', StartPage.as_view(), name="startpage"),
    url(r'profiles/', ProfileList.as_view(), name="profiles"),
    url(r'profile/id(?P<pk>\d+)/', ProfileMainDetail.as_view(), name="profile_main_page"),
    # url(r'profile/id(?P<pk>\d+)/blogs/', ProfileBlogsDetail.as_view(), name="profile_blogs"),
    # url(r'profile/id(?P<pk>\d+)/posts/', ProfilePostsDetail.as_view(), name="profile_posts"),
    # url(r'profile/id(?P<pk>\d+)/comments/', ProfileCommentsDetail.as_view(), name="profile_main_page")
]
