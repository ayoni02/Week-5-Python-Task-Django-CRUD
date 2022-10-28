from msilib.schema import Class
from django.db import models

# Create your models here.

class Artist(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
class Lyric(models.Model):
    content = models.CharField(max_length=200)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)