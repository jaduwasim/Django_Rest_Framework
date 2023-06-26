from rest_framework import serializers
from .models import Album, Musician

class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class MusicianSerializers(serializers.ModelSerializer):
    album_musician = AlbumSerializers(read_only=True, many=True)
    class Meta:
        model = Musician
        fields = '__all__'