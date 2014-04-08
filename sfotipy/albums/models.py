from django.db import models

from artists.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='albums')
    artist = models.ForeignKey(Artist)