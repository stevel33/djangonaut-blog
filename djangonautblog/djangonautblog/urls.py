from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # r = raw string, ^ = has to be start of string, $ = end of string
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    # ^$ looks out for just .com
    url(r'^$', views.homepage)
]
