from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import MovieDetail, CommentListSerialize, MovieCreateSerializer
from .models import Movie, Comment, MBTI

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)

    serializer = MovieDetail(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def movie_create(request):
    serializer = MovieCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, movie_id=movie_pk)

    serializer = MovieDetail(movie)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, movie_id=movie_pk)
    serializer = CommentListSerialize(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie, username=request.user.username)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.comment.filter(pk=comment_pk).exists():
        return Response({'detail': '댓글을 쓰신 분이 아니군요?'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = CommentListSerialize(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentListSerialize(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({'pk': f'{comment_pk}가 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def mbti_set(request, movie_pk, mbti_type):
    movie = get_object_or_404(Movie, movie_id=movie_pk)
    mbti = get_object_or_404(MBTI, mbti=mbti_type)
    movie.mbti.add(mbti)
    return Response({'mbti': f'{movie_pk}에 {mbti_type}이 추가되었습니다.'})
