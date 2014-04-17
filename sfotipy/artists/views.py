from django.shortcuts import render

from django.views.generic.detail import DetailView

from .models import Artist

# detalle de un artista
class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'

    def get_template_names(self):
	return 'artist.html'