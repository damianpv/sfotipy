from django.test import TestCase

from .models import Artist
from tracks.models import Track
from albums.models import Album

class TestArtist(TestCase):

    def setUp(self):
	self.artist = Artist.objects.create(first_name='david', last_name='bowie')
	self.album = Album.objects.create(title='heroes', artist=self.artist)
	self.track = Track.objects.create(title='heroes', artist=self.artist, album=self.album, order=1, track_file='media/test')
    
    def test_existe_vista(self):
	res = self.client.get('/artists/%d' % self.artist.id)
	self.assertEqual(res.status_code, 200)
	self.assertTrue('david' in res.content)

    def test_usuario_logueado(self):
	res = self.client.get('/tracks/%s' % self.track.title)
	self.assertEqual(res.status_code, 301)

    def test_no_existe_vista(self):
	id_viejo = self.artist.id
	self.artist.delete()
	res = self.client.get('/artists/%d' % id_viejo)
	self.assertEqual(res.status_code, 404)



