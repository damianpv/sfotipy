from django.contrib import admin

from .models import Artist

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', )

admin.site.register(Artist, ArtistAdmin)