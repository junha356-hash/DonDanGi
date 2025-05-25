# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from products.models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from user.models import Profile

class AIRecommendView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            return Response({"error": "프로필이 없습니다."}, status=404)

        # 예) 단순: 최고 금리 예금/적금 추천 (실제 AI 로직은 자유롭게)
        deposit_option = DepositOptions.objects.order_by('-intr_rate').first()
        saving_option = SavingOptions.objects.order_by('-intr_rate').first()
        
        deposit_product = deposit_option.fin_prdt_cd if deposit_option else None
        saving_product = saving_option.fin_prdt_cd if saving_option else None

        # 추천 이유 작성 (실제 투자성향/risk_profile에 따라 문구 등 커스텀 가능)
        deposit_reason = f"{profile.age}세, {profile.risk_profile} 성향, 자산 {profile.liquid_assets}만원, 연봉 {profile.annual_income}만원에 적합한 최고 금리 예금입니다."
        saving_reason = f"{profile.age}세, {profile.risk_profile} 성향, 자산 {profile.liquid_assets}만원, 연봉 {profile.annual_income}만원에 적합한 최고 금리 적금입니다."
        
        result = {
            "예금": {
                "상품 이름": deposit_product.fin_prdt_nm if deposit_product else "",
                "은행": deposit_product.kor_co_nm if deposit_product else "",
                "옵션": deposit_option.intr_rate_type_nm if deposit_option else "",
                "금리": deposit_option.intr_rate if deposit_option else "",
                "저축 기간": deposit_option.save_trm if deposit_option else "",
                "추천 이유": deposit_reason,
            },
            "적금": {
                "상품 이름": saving_product.fin_prdt_nm if saving_product else "",
                "은행": saving_product.kor_co_nm if saving_product else "",
                "옵션": saving_option.intr_rate_type_nm if saving_option else "",
                "금리": saving_option.intr_rate if saving_option else "",
                "저축 기간": saving_option.save_trm if saving_option else "",
                "추천 이유": saving_reason,
            }
        }
        return Response(result)
