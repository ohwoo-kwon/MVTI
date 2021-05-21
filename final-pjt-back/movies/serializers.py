from rest_framework import serializers
from rest_framework.views import exception_handler
from .models import Movie, Comment, MBTI

class MovieCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class CommentListSerialize(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username')

class MBTISerializer(serializers.ModelSerializer):

    class Meta:
        model = MBTI
        fields = ('mbti',)

class MovieDetail(serializers.ModelSerializer):
    comment_set = CommentListSerialize(many=True, read_only=True)
    mbti = MBTISerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'