# user/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from .models import Profile

# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def user_profile_view(request, pk):
#     profile = request.user.profile
#     if request.method == 'GET':
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProfileSerializer(profile, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    user = request.user
    # 프로필이 없으면 생성
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)