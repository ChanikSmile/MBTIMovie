<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 3.2.18 on 2023-05-23 23:44
=======
# Generated by Django 3.2.18 on 2023-05-24 05:02
>>>>>>> fetch_jo
=======
# Generated by Django 3.2.18 on 2023-05-24 16:22
>>>>>>> fetch_jun
=======
# Generated by Django 3.2.18 on 2023-05-25 03:00
>>>>>>> fetch_jo

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('community_user_like', models.ManyToManyField(blank=True, related_name='like_community', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('release_date', models.DateTimeField()),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.TextField()),
                ('video', models.TextField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genre_ids', models.TextField()),
                ('backdrop_path', models.TextField()),
                ('adult', models.TextField()),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                ('movie_user_like', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
=======
                ('genre_check', models.ManyToManyField(related_name='genre_movies', to='movies.Genre')),
                ('movie_user_like', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
>>>>>>> fetch_jo
=======
                ('f_user_like', models.ManyToManyField(blank=True, related_name='f_like_movies', to=settings.AUTH_USER_MODEL)),
=======
                ('f_user_like', models.ManyToManyField(blank=True, related_name='f_like_movies', to=settings.AUTH_USER_MODEL)),
                ('genre_check', models.ManyToManyField(related_name='genre_movies', to='movies.Genre')),
>>>>>>> fetch_jo
                ('movie_user_like', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('n_user_like', models.ManyToManyField(blank=True, related_name='n_like_movies', to=settings.AUTH_USER_MODEL)),
                ('s_user_like', models.ManyToManyField(blank=True, related_name='s_like_movies', to=settings.AUTH_USER_MODEL)),
                ('t_user_like', models.ManyToManyField(blank=True, related_name='t_like_movies', to=settings.AUTH_USER_MODEL)),
<<<<<<< HEAD
>>>>>>> fetch_jun
=======
>>>>>>> fetch_jo
            ],
        ),
        migrations.CreateModel(
            name='Community_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.community')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
