from django.conf.urls import url
from like.views import *

urlpatterns = [
    url(r'^like/$', like_something, name="like"),
]