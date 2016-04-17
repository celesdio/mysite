"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from learn import views as learn_views
from calc import views as calc_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',learn_views.home,name='home'),
    url(r'^add/',calc_views.add ,name='add'),
    url(r'^add2/(\d+)/(\d+)$',calc_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)$',calc_views.add2,name='add2'),
]

# urlpatterns = patterns('',
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^blog/$', 'blog.views.index'),
#     url(r'^$','learn.views.index'),
# )