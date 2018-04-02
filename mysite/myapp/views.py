from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Album
from .models import song
from django.db.models import Count

from django import forms

from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('index')
    else:
        return HttpResponseRedirect('login')


@login_required(login_url='login')
def register(request):
    return render(request, 'app/register.html')


@login_required(login_url='login')
def contact_us(request):
        return render(request, 'app/contact_us.html')


@login_required(login_url='login')
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums, }
    return render(request, 'app/index.html',context)


@login_required(login_url='login')
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'app/detail.html', {'album': album, })


@login_required(login_url='login')
def favorite(request, album_id):
    #import ipdb; ipdb.set_trace()
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, album.song.DoesNotExist):
        return render(request, 'app/detail.html', {
           'album': album,
           'error_message': "Sorry not working",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'app/detail.html', {'album': album, })


def add_new_album(request):
    return render(request, 'app/add_new_album.html')


def add_album(request):
    album = Album()
    album.album_title = request.POST['album_title']
    album.artist = request.POST['artist']
    album.gerne = request.POST['gerne']
    album.album_logo = request.POST['album_logo']
    album.save()
    return HttpResponseRedirect('index')


def add_new_song(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    return render(request, 'app/add_new_song.html', {'album': album, })


def add_song(request):
    song_set_data = song()
    song_set_data.album_id = request.POST['album']
    song_set_data.song_title = request.POST['song_title']
    song_set_data.file_type = request.POST['file_type']
    song_set_data.save()
    return HttpResponseRedirect('index')


def delete_album(request, album_id):
    instance = Album.objects.get(pk=album_id)
    instance.delete()
    return HttpResponseRedirect('/app/index')


def delete_song(request, song_id):
    instance = song.objects.get(pk=song_id)
    instance.delete()
    return HttpResponseRedirect('/app/index')