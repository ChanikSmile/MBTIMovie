from . import views
from django.urls import path

urlpatterns = [
	path('movies/', views.movie_list),
	path('movies/<int:movie_pk>/', views.movie_detail),
	path('comments/', views.comment_list),
	path('comments/<int:comment_pk>/', views.comment_detail),
	path('movies/<int:movie_pk>/comments/', views.create_comment),
	path('<int:movie_pk>/likes/', views.likes, name='likes'),
	path('community/', views.community_list),
	path('community/<int:community_pk>/', views.community_detail),
	# path('community/create/', views.create_community),
	path('community/<int:community_pk>/comments/<int:comment_pk>', views.community_comment_delete),
]
