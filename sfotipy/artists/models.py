from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    favorite_songs = models.ManyToManyField('tracks.Track', blank=True, related_name='is_favorite_of')

    def es_pharrel(self):
        return self.id == 1

    def __unicode__(self):
        return self.first_name

#from django.core.cache import cache
#from django.db.models.signals import post_save
#from django.contrib.sessions.models import Session
#from django.dispatch import receiver

#@receiver(post_save)
#def clear_cache(sender, **kwargs):
#    if sender != Session:
#        cache._cache.flush_all()