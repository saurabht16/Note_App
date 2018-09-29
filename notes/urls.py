from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^list/$', views.notes_list, name='notes_list'),
    url(r'^detail/(?P<id>\d+)/$', views.notes_detail,name='notes_detail'),
]