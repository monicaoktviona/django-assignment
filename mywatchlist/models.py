from django.db import models

# Create your models here.
class WatchlistMovie(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=100)
    review = models.TextField()