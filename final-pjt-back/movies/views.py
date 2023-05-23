from django.shortcuts import render, redirect
from .models import Movie, Comment, Community, Community_comment

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, CommentListSerializer
from .serializers import CommunityListSerializer, CommunitySerializer, CommunityCommentSerializer, CommunityCommentListSerializer

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

@api_view(['GET', 'POST'])
def community_list(request):
    if request.method == "GET":
        community_lists = Community.objects.all()
        serializer = CommunityListSerializer(community_lists, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        user = get_user_model().objects.get(username=request.user)
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# @login_required # 로그인된 사용자만 접근할 수 있도록 설정
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    
    if request.method == "GET":
        comments = community.comments.all()
        serializer = CommunitySerializer(community)
        comments_serializer = CommunityCommentSerializer(comments, many=True)
        context = {
            'community': serializer.data,
            'comments': comments_serializer.data,
        }
        return Response(context)

    elif request.method == "DELETE":
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        user = get_user_model().objects.get(username=request.user)
        
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(community=community, user=user)
            return Response(serializer.data)

    elif request.method == "POST":
        user = get_user_model().objects.get(username=request.user)
        
        serializer = CommunityCommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(community=community, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
# @api_view(['GET', 'POST'])
# def create_community(request):
#     serializer = CommunitySerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

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
def community_likes(request, community_pk):
	if request.user.is_authenticated:
		community = get_object_or_404(Community, pk=community_pk)
		serializer = CommunitySerializer(community)
		if serializer.is_valid(raise_exception=True): 
			if community.community_user_like.filter(pk=request.user.pk).exists():
				community.community_user_like.remove(request.user)
			else:
				community.community_user_like.add(request.user)
			serializer.save(community=community)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','DELETE', 'PUT'])
def community_comment_delete(request, community_pk, comment_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comment = get_object_or_404(Community_comment, pk=comment_pk, community_id=community_pk)
    if request.method == "GET":
        serializer = CommunityCommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
    
    elif request.method == "PUT":
        user = get_user_model().objects.get(username=request.user)
        print(user)
        serializer = CommunityCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(community=community, user=user)
            return Response(serializer.data)
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_204_NO_CONTENT)
