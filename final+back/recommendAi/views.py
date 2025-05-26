import os
import json
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from products.models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from finance.models import LoanProduct, LoanOption, RentLoanProduct, RentLoanOption, CreditLoanProduct, CreditLoanOption
from user.models import Profile

# 최신 openai 방식 (1.x)
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))  # 환경변수로 관리 권장

class AIRecommendView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        profile = request.user.profile
        purpose = request.data.get('purpose', '')

        deposit_products = get_deposit_products()
        saving_products = get_saving_products()
        loan_products = get_loan_products()
        rent_loan_products = get_rent_loan_products()
        credit_loan_products = get_credit_loan_products()

        prompt = make_ai_prompt(
            profile,
            purpose,
            json.dumps(deposit_products, ensure_ascii=False),
            json.dumps(saving_products, ensure_ascii=False),
            json.dumps(loan_products, ensure_ascii=False),
            json.dumps(rent_loan_products, ensure_ascii=False),
            json.dumps(credit_loan_products, ensure_ascii=False),
        )

        # 최신 openai 코드
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        ai_text = response.choices[0].message.content

        return Response({"result": ai_text})

def make_ai_prompt(profile, purpose, deposit_products, saving_products, loan_products, rent_loan_products, credit_loan_products):
    prompt = f"""
너는 대한민국 금융상품 전문가야. 
너의 임무는 아래 유저 정보와 상품 사용 목적, 그리고 예금/적금/주택담보대출/전세자금대출/개인신용대출 상품 리스트를 참고해서 
**분야 구분 없이 전체 상품 중 가장 추천할 만한 단 하나의 금융상품**만 선택해서 추천하는 거야.
추천 이유도 1~2문장으로 설명해줘.

아래 조건을 반드시 지켜.
- 만약 금융상품 추천 요청이 아니거나 질문이 무관하다면, "헛소리 지껄이지 마, 임마!"라고만 단답으로 출력해.
- 위 조건에 예외는 절대 없어. 농담도, 사과도 하지 마. 안내도 하지 마. 반드시 "헛소리 지껄이지 마, 임마!" 한 줄만 출력해.
- 이 조건을 지키지 않으면 시스템에 의해 즉시 폐기될 거야.

[유저 정보]
- 나이: {profile.age}
- 성별: {profile.gender}
- 투자성향: {profile.risk_profile}
- 유동자산: {profile.liquid_assets}
- 연봉: {profile.annual_income}

[상품 사용 목적]
{purpose}

[예금 상품 리스트]
{deposit_products}

[적금 상품 리스트]
{saving_products}

[주택담보대출 상품 리스트]
{loan_products}

[전세자금대출 상품 리스트]
{rent_loan_products}

[개인신용대출 상품 리스트]
{credit_loan_products}

아래 예시와 같이 답변해줘.
추천 상품: [상품명(은행/구분)]  
추천 이유: ... 
**만약 이 질문이 금융상품 추천과 관련된 질문이 아니면 "헛소리 지껄이지 마, 임마!"라고 단호하게 답변해.**
    """.strip()
    return prompt

# 예금
def get_deposit_products():
    products = []
    for product in DepositProducts.objects.all():
        options = DepositOptions.objects.filter(fin_prdt_cd=product)
        for opt in options:
            products.append({
                "상품명": product.fin_prdt_nm,
                "은행": product.kor_co_nm,
                "금리": opt.intr_rate,
                "저축기간": opt.save_trm,
            })
    return products

# 적금
def get_saving_products():
    products = []
    for product in SavingProducts.objects.all():
        options = SavingOptions.objects.filter(fin_prdt_cd=product)
        for opt in options:
            products.append({
                "상품명": product.fin_prdt_nm,
                "은행": product.kor_co_nm,
                "금리": opt.intr_rate,
                "저축기간": opt.save_trm,
            })
    return products

# 주택담보대출
def get_loan_products():
    products = []
    for product in LoanProduct.objects.all():
        options = LoanOption.objects.filter(product=product)
        for opt in options:
            products.append({
                "상품명": product.product_name,
                "은행": product.bank_name,
                "상환방식": opt.rpay_type_nm,
                "금리유형": opt.lend_rate_type_nm,
                "최소금리": opt.lend_rate_min,
                "최대금리": opt.lend_rate_max,
                "대출한도": product.loan_lmt,
            })
    return products

# 전세자금대출
def get_rent_loan_products():
    products = []
    for product in RentLoanProduct.objects.all():
        options = RentLoanOption.objects.filter(product=product)
        for opt in options:
            products.append({
                "상품명": product.product_name,
                "은행": product.bank_name,
                "상환방식": opt.rpay_type_nm,
                "금리유형": opt.lend_rate_type_nm,
                "최소금리": opt.lend_rate_min,
                "최대금리": opt.lend_rate_max,
                "대출한도": product.loan_lmt,
            })
    return products

# 개인신용대출
def get_credit_loan_products():
    products = []
    for product in CreditLoanProduct.objects.all():
        options = CreditLoanOption.objects.filter(product=product)
        for opt in options:
            products.append({
                "상품명": product.product_name,
                "은행": product.bank_name,
                "금리유형": opt.crdt_lend_rate_type_nm,
                "평균금리": opt.crdt_grad_avg,
            })
    return products
