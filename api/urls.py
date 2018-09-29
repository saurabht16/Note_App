from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls import include
from . import views


urlpatterns = [
    url('rest-auth/', include('rest_auth.urls')),
    url(r'^(?P<pk>\d+)/$', views.DetailNotes.as_view()),
    url('^labels/(?P<labels>.+)/$', views.LabelSearch.as_view()),
    url('', views.ListNotes.as_view()),


]