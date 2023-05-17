from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    original_language = models.TextField()
    original_title = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    video = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genre_ids = models.TextField()
    backdrop_path = models.TextField()
    adult = models.TextField()
    id = models.IntegerField(primary_key=True)

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

