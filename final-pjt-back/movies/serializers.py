from rest_framework import serializers
from .models import Movie, Genre, Comment, Community, Community_comment
from accounts.serializers import UserSerializer

class Movie2(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'genre_ids')
        read_only_fields = ('overview',)


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)
        
class CommunityListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ('user',)

class CommunityCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community_comment
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    movie = Movie2(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)

class CommunityCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Community_comment
        fields = ('user', 'content', 'id')
        read_only_fields = ('community', 'user')

class CommunitySerializer(serializers.ModelSerializer):
    comment_set = CommunityCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Community
        fields = '__all__'
