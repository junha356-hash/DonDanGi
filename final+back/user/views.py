from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from .models import Profile
from products.models import DepositProducts, SavingProducts
from .serializers import ProfileSerializer

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
    
    
class UserProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 내 상품 리스트 반환
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response({
            "deposits": serializer.data["my_deposits"],
            "savings": serializer.data["my_savings"]
        })

    def post(self, request):
        # 상품 추가
        profile = request.user.profile
        type_ = request.data.get("type")
        fin_prdt_cd = request.data.get("fin_prdt_cd")
        if type_ == "deposit":
            try:
                product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
                profile.my_deposits.add(product)
            except DepositProducts.DoesNotExist:
                return Response({"error": "해당 예금 상품이 없습니다."}, status=404)
        elif type_ == "saving":
            try:
                product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
                profile.my_savings.add(product)
            except SavingProducts.DoesNotExist:
                return Response({"error": "해당 적금 상품이 없습니다."}, status=404)
        else:
            return Response({"error": "type 값이 잘못됨"}, status=400)
        return Response({"message": "상품이 추가되었습니다."}, status=201)

    def delete(self, request):
        # 상품 제거
        profile = request.user.profile
        type_ = request.query_params.get("type")
        fin_prdt_cd = request.query_params.get("fin_prdt_cd")
        if type_ == "deposit":
            try:
                product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
                profile.my_deposits.remove(product)
            except DepositProducts.DoesNotExist:
                return Response({"error": "해당 예금 상품이 없습니다."}, status=404)
        elif type_ == "saving":
            try:
                product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
                profile.my_savings.remove(product)
            except SavingProducts.DoesNotExist:
                return Response({"error": "해당 적금 상품이 없습니다."}, status=404)
        else:
            return Response({"error": "type 값이 잘못됨"}, status=400)
        return Response({"message": "상품이 삭제되었습니다."}, status=200)