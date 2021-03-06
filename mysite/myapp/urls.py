from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^index$', views.index),
    url(r'^logout/$', auth_views.logout, {'template_name': 'app/login.html'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}, name='login'),
    url(r'^register$', views.register),
    url(r'^contact_us$', views.contact_us),
    url(r'^add_new_album$', views.add_new_album),
    url(r'^add_new_song/(?P<album_pk>[0-9]+)$', views.add_new_song),
    url(r'^add_album$', views.add_album, name="add_album"),
    url(r'^add_song$', views.add_song, name="add_song"),
    url(r'^delete_song/(?P<song_id>[0-9]+)$', views.delete_song),
    url(r'^delete_album/(?P<album_id>[0-9]+)$', views.delete_album),
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name="details"),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite")
]


