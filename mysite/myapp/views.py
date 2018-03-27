from django.shortcuts import render
from django.http import Http404
from .models import Album
from django.shortcuts import render, get_object_or_404

# Create your views here.


def login(request):
    return render(request, 'app/login.html')


def register(request):
    return render(request, 'app/register.html')

def contact_us(request):
    return render(request, 'app/contact_us.html')


def index(request):

    all_albums = Album.objects.all()
    context = {'all_albums': all_albums, }
    return render(request, 'app/index.html',context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'app/detail.html', {'album': album,})


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
