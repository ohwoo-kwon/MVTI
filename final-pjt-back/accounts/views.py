from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.shortcuts import render
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')

    # 비밀번호가 일치하지 않은 경우
    if password != passwordConfirmation:
        return Response({"detail" : "비밀번호가 일치하지 않습니다"}, status=status.HTTP_400_BAD_REQUEST)
    
    # 직렬화
    serializer = UserSerializer(data=request.data)

    # 유효한지 확인
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)