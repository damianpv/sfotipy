import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
#from artists.tasks import demorada
from .models import Track

import time # redis cache: test

# redis cache
from django.core.cache import cache

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

    # redis cache : low level
    data = cache.get('data_%s' % title)
    if data is None:

        data = {
            'title': track.title,
            'order': track.order,
            'album': track.album.title,
            'artist': {
                'name': track.artist.first_name,
                'bio': bio,
            }
        }
        time.sleep(5)
        cache.set('data_%s' % title, data)

    #time.sleep(5) # redis cache: test

    #demorada.apply_async(countdown=5)

    #json_data = json.dumps(data) # diccionario de python a json
    #json.loads(string_json) # json a diccionario de python

    #return HttpResponse(json_data, content_type='application/json')
    return render(request, 'track.html', {'track': track, 'bio': bio})


from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
    model = Track