from django.shortcuts import render

from rest_framework import viewsets

from .models import Album

class AlbumViewSet(viewsets.ModelViewSet):
    model = Album