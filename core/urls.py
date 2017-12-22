
from django.conf.urls import url
from core.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^gbase/$', g_base_view, name="gbase"),
    url(r'^main_page/$', StartPage.as_view(), name="startpage"),
    url(r'^profiles/$', ProfileList.as_view(), name="profiles"),
    url(r'^profile/id(?P<pk>\d+)/$', ProfileMainDetail.as_view(), name="profile_main_page"),
    url(r'^login/$', LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name="logout.html"), name="logout"),
    url(r'^signup/$', ProfileCreate.as_view(), name="signup"),
    url(r'^profile/edit/$', login_required(ProfileUpdate.as_view()), name="profile_update"),
    url(r'^profile/chpw/$', login_required(ProfileUpdatePass.as_view()), name="profile_update_pass"),
    url(r'profile/id(?P<pk>\d+)/blogs/', ProfileBlogList.as_view(), name="profile_blogs"),
    url(r'profile/id(?P<pk>\d+)/posts/', ProfilePostList.as_view(), name="profile_posts"),
    url(r'profile/id(?P<pk>\d+)/comments/', ProfileCommentList.as_view(), name="profile_comments"),
    url(r'profile/id(?P<pk>\d+)/favorites/', ProfileFavoriteList.as_view(), name="profile_favorites")
]
