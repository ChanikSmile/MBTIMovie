from django.contrib import admin
from .models import Movie, Comment
# Register your models here.

admin.site.register(Comment)
admin.site.register(Movie)
