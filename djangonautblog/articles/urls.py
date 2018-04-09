from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'articles'

urlpatterns = [
    # r = raw string, ^ = has to be start of string, $ = end of string
    # ^$ looks out for just .com
    # (?P) = named capturing group
    # \w- any kind of letter or hyphen .. + means any length
    url(r'^$', views.article_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]
