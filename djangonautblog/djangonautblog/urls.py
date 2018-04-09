from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # r = raw string, ^ = has to be start of string, $ = end of string
    # ^$ looks out for just .com
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage) 
]

urlpatterns += staticfiles_urlpatterns()