# user/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProfileSerializer

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    profile = request.user.profile
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
