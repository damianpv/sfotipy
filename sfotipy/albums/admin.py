from django.contrib import admin

from .models import Album
from sorl.thumbnail import get_thumbnail

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'imagen_album')

    def imagen_album(self, obj):
        return '<img src="%s">' % get_thumbnail(obj.cover, '50x150', format='PNG').url # , crop='center'
    imagen_album.allow_tags = True

admin.site.register(Album, AlbumAdmin)