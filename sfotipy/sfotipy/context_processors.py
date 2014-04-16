from random import choice

frase = ['hello', 'hola', 'hi']

from tracks.models import Track

def basico(request):
    tracks = Track.objects.all()
    track = None

    #import ipdb;ipdb.set_trace()

    for t in tracks:
	if request.path == t.get_absolute_url():
	    track = t
	    break
    return {'titulo': choice(frase), 'tracks': tracks, 'selected_track':track}