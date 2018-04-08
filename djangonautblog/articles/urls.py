from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # r = raw string, ^ = has to be start of string, $ = end of string
    # ^$ looks out for just .com
    url(r'^$', views.article_list)
]
