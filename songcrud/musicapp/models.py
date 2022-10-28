from msilib.schema import Class
from django.db import models

# Create your models here.

class Artist(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    
    def __str__(self):
        return self.First_name + " " + self.Last_name
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)