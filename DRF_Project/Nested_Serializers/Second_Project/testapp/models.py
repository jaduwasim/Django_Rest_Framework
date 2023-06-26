from django.db import models
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    instrument = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'Musician'
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_musician', null=True)
    name = models.CharField(max_length=64)
    release_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Album'

