# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.noticia_list, name='noticia_list'),
    url(r'^posts/(?P<slug>[\w_-]+)/$', views.post, name='post'),
]