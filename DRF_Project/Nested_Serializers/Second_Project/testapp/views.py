from django.shortcuts import render
from .models import Album, Musician
from .serializers import MusicianSerializers, AlbumSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class AlbumListCreateAPIView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

class AlbumRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

class MusicianListCreateAPIView(ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers

class MusicianRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers