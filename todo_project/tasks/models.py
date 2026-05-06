from django.db import models

# Create your models here.

class Song(models.Model):
    title =  models.CharField(max_length=200) 
    artist = models.CharField(max_length=200)
    snippet = models.TextField()
    second_snippet = models.TextField(blank=True, null=True)
    full_lyrics = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.artist}"