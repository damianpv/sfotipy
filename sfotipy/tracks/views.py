import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import Track

@login_required
def track_view(request, title):

    #import ipdb; ipdb.set_trace(); # Debug de codigo

    '''
    try:
        track = Track.objects.get(title=title)
    except Track.DoesNotExist:
        raise Http404
    '''

    track = get_object_or_404(Track, title=title)
    bio = track.artist.biography

    data = {
        'title': track.title,
        'order': track.order,
        'album': track.album.title,
        'artist': {
            'name': track.artist.first_name,
            'bio': bio,
        }
    }

    #json_data = json.dumps(data) # diccionario de python a json
    #json.loads(string_json) # json a diccionario de python

    #return HttpResponse(json_data, content_type='application/json')
    return render(request, 'track.html', {'track': track, 'bio': bio})