from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def signup(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()  # 사용자 데이터 저장
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)