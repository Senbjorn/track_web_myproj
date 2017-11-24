
from django.conf.urls import url
from core.views import *
from django.contrib.auth.views import login, logout, LoginView, LogoutView

urlpatterns = [
    url(r'^main_page/$', StartPage.as_view(), name="startpage"),
    url(r'^profiles/$', ProfileList.as_view(), name="profiles"),
    url(r'^profile/id(?P<pk>\d+)/$', ProfileMainDetail.as_view(), name="profile_main_page"),
    url(r'^login/$', LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name="logout.html"), name="logout"),
    url(r'^signup/$', ProfileCreate.as_view(), name="signup"),
    url(r'^profile/id(?P<pk>\d+)/edit/$', ProfileMainDetail.as_view(), name="profile_update")
    # url(r'profile/id(?P<pk>\d+)/blogs/', ProfileBlogsDetail.as_view(), name="profile_blogs"),
    # url(r'profile/id(?P<pk>\d+)/posts/', ProfilePostsDetail.as_view(), name="profile_posts"),
    # url(r'profile/id(?P<pk>\d+)/comments/', ProfileCommentsDetail.as_view(), name="profile_main_page")
]
