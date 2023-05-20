from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def signup(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()  # 사용자 데이터 저장	
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_accounts(request):
    User = get_user_model()
    users = User.objects.all()

    data = []
    for user in users:
        data.append({
            'username': user.username,
            'user_id': user.pk,
            'genders': user.genders,  # 새로운 필드
            'mbtis': user.mbtis,  # 새로운 필드
        })

    return JsonResponse(data, safe=False)


