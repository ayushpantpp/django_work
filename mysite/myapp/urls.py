from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^index$', views.index),
    #url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'app/login.html'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),

    #url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^contact_us$', views.contact_us),
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name="details"),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite")
]


