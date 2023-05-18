from . import views
from django.urls import path

urlpatterns = [
	path('movies/', views.movie_list),
	path('movies/<int:movie_pk>/', views.movie_detail),
	path('comments/', views.comment_list),
	path('comments/<int:comment_pk>/', views.comment_detail),
	path('movies/<int:movie_pk>/comments/', views.create_comment),
	path('<int:movie_pk>/likes/', views.likes, name='likes'),
	path('community_comments/', views.community_comment_list),
	path('community_comments/<int:community_comment_pk>/', views.community_comment_detail),
	path('community_comments/create/', views.create_community_comment),
]
