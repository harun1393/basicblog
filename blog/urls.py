from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='blog-home'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<category_name_slug>[\w-]+)/$', views.category, name='category'),
]
