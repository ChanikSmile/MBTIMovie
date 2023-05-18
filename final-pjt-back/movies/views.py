from django.shortcuts import render, redirect
from .models import Movie, Comment, Community_comment

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.http import require_POST, require_GET

from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, CommentListSerializer
from .serializers import CommunityCommentListSerializer, CommunityCommentSerializer

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movie_lists = Movie.objects.all()
    serializer = MovieListSerializer(movie_lists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    comment_lists = Comment.objects.all()
    serializer = CommentListSerializer(comment_lists, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def community_comment_list(request):
    community_comment_lists = Community_comment.objects.all()
    serializer = CommunityCommentListSerializer(community_comment_lists, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT', 'DELETE'])
def community_comment_detail(request, community_comment_pk):
    community_comment = get_object_or_404(Community_comment, pk=community_comment_pk)
    if request.method == "GET":
        serializer = CommunityCommentSerializer(community_comment)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        community_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = CommunityCommentSerializer(community_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def create_community_comment(request):
    serializer = CommunityCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def likes(request, movie_pk):
	if request.user.is_authenticated:
		movie = get_object_or_404(Movie, pk=movie_pk)
		serializer = MovieSerializer(movie)
		if serializer.is_valid(raise_exception=True): 
			if movie.movie_user_like.filter(pk=request.user.pk).exists():
				movie.movie_user_like.remove(request.user)
			else:
				movie.movie_user_like.add(request.user)
			serializer.save(movie=movie)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def community_likes(request, community_comment_pk):
	if request.user.is_authenticated:
		community_comment = get_object_or_404(Community_comment, pk=community_comment_pk)
		serializer = CommunityCommentSerializer(community_comment)
		if serializer.is_valid(raise_exception=True): 
			if community_comment.community_user_like.filter(pk=request.user.pk).exists():
				community_comment.community_user_like.remove(request.user)
			else:
				community_comment.community_user_like.add(request.user)
			serializer.save(community_comment=community_comment)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_401_UNAUTHORIZED)
