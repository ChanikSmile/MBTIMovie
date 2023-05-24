from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
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
    # movie_id = models.IntegerField()
    
class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    community_user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_community', blank=True)

class Community_comment(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)