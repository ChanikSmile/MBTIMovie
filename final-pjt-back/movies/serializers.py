from rest_framework import serializers
from .models import Movie, Comment, Community_comment


class Movie2(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class MovieListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('title', 'overview')
		read_only_fields = ('overview',)


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title', 'content')
        
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
    
    class Meta:
        model = Comment
        fields = ('id', 'movie', 'title', 'content',)


class CommunityCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Community_comment
        fields = '__all__'