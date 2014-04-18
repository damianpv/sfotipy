from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .models import Artist

# detalle de un artista
class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'

    def get_template_names(self):
	return 'artist.html'

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'artists.html'

from rest_framework import viewsets
from .serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    model = Artist
    serializer_class = ArtistSerializer
    filter_fields = ('id', )
    paginate_by = 1


from django.contrib.auth.models import User, Group