# finance/views.py 일부 예시
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import LoanProduct, LoanOption, RentLoanProduct, RentLoanOption, CreditLoanProduct, CreditLoanOption, DepositProducts,DepositOptions,SavingOptions,SavingProducts
from django.views.decorators.csrf import csrf_exempt
import openai
import json
from user.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DepositProductsSerializer,DepositOptionsSerializer,SavingProductsSerializer,SavingOptionsSerializer
from django.shortcuts import get_object_or_404,get_list_or_404

# 주택담보대출 
@csrf_exempt
def fetch_loan_products(request):
    api_url = 'http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json'
    api_key = settings.FSS_API_KEY
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',  # 은행
        'pageNo': 1
    }
    resp = requests.get(api_url, params=params)
    data = resp.json()
    base_list = data['result']['baseList']
    option_list = data['result']['optionList']

    # 1. baseList(기본정보) 저장
    for base in base_list:
        product, created = LoanProduct.objects.update_or_create(
            product_code=base['fin_prdt_cd'],
            defaults={
                'product_name': base.get('fin_prdt_nm'),
                'bank_name': base.get('kor_co_nm'),
                'loan_type': '주택담보',
                'loan_lmt': base.get('loan_lmt'),
                'dly_rate': base.get('dly_rate'),
                'erly_rpay_fee': base.get('erly_rpay_fee'),
                'join_way': base.get('join_way'),
            }
        )
        # 2. optionList(옵션) 저장
        for option in option_list:
            if option['fin_prdt_cd'] == product.product_code:
                LoanOption.objects.update_or_create(
                    product=product,
                    defaults={
                        'rpay_type_nm': option.get('rpay_type_nm'),
                        'lend_rate_type_nm': option.get('lend_rate_type_nm'),
                        'lend_rate_min': option.get('lend_rate_min') or None,
                        'lend_rate_max': option.get('lend_rate_max') or None,
                }
            )
    return JsonResponse({'status': 'ok', 'count': len(base_list)})  

def loan_product_list(request):
    result = []
    products = LoanProduct.objects.all()
    for product in products:

    # 각 상품에 연결된 모든 옵션을 리스트로 추출
        options = product.options.all().values(
            'mrtg_type', 'mrtg_type_nm',
            'rpay_type', 'rpay_type_nm',
            'lend_rate_type', 'lend_rate_type_nm',
            'lend_rate_min', 'lend_rate_max', 'lend_rate_avg'
    )
        result.append({
            'product_code': product.product_code,
            'product_name': product.product_name,
            'bank_name': product.bank_name,
            'loan_type': product.loan_type,
            'join_way': product.join_way,
            'loan_inci_expn': product.loan_inci_expn,
            'erly_rpay_fee': product.erly_rpay_fee,
            'dly_rate': product.dly_rate,
            'loan_lmt': product.loan_lmt,
            'dcls_month': product.dcls_month,
            'dcls_strt_day': product.dcls_strt_day,
            'dcls_end_day': product.dcls_end_day,
            'fin_co_subm_day': product.fin_co_subm_day,
            'options': list(options),
    })
    return JsonResponse(result, safe=False)

# 전세자금대출 
@csrf_exempt
def fetch_rent_loan_products(request):
    api_url = 'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json'
    api_key = settings.FSS_API_KEY
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',  # 은행
        'pageNo': 1
    }
    resp = requests.get(api_url, params=params)
    data = resp.json()
    base_list = data['result']['baseList']
    option_list = data['result']['optionList']

    for base in base_list:
        product, created = RentLoanProduct.objects.update_or_create(
            product_code=base['fin_prdt_cd'],
            defaults={
            'product_name': base.get('fin_prdt_nm'),
            'bank_name': base.get('kor_co_nm'),
            'join_way': base.get('join_way'),
            'erly_rpay_fee': base.get('erly_rpay_fee'),
            'dly_rate': base.get('dly_rate'),
            'loan_lmt': base.get('loan_lmt'),
        }
)

        for option in option_list:
            if option['fin_prdt_cd'] == product.product_code:
                RentLoanOption.objects.update_or_create(
                    product=product,
                    defaults={
                    'rpay_type_nm': option.get('rpay_type_nm'),
                    'lend_rate_type_nm': option.get('lend_rate_type_nm'),
                    'lend_rate_min': option.get('lend_rate_min') or None,
                    'lend_rate_max': option.get('lend_rate_max') or None,
                }
        )
    return JsonResponse({'status': 'ok', 'count': len(base_list)})

def rent_loan_product_list(request):
    result = []
    products = RentLoanProduct.objects.all()
    for product in products:
        options = product.options.all().values(
            'rpay_type', 'rpay_type_nm',
            'lend_rate_type', 'lend_rate_type_nm',
            'lend_rate_min', 'lend_rate_max', 'lend_rate_avg'
        )
        result.append({
            'product_code': product.product_code,
            'product_name': product.product_name,
            'bank_name': product.bank_name,
            'fin_co_no': product.fin_co_no,
            'loan_type': product.loan_type,
            'join_way': product.join_way,
            'loan_inci_expn': product.loan_inci_expn,
            'erly_rpay_fee': product.erly_rpay_fee,
            'dly_rate': product.dly_rate,
            'loan_lmt': product.loan_lmt,
            'dcls_month': product.dcls_month,
            'dcls_strt_day': product.dcls_strt_day,
            'dcls_end_day': product.dcls_end_day,
            'fin_co_subm_day': product.fin_co_subm_day,
            'options': list(options),
        })
    return JsonResponse(result, safe=False)

# 개인신용대출 
@csrf_exempt
def fetch_credit_loan_products(request):
    api_url = 'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json'
    api_key = settings.FSS_API_KEY
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',  # 은행, 필요에 따라 조정
        'pageNo': 1
    }
    resp = requests.get(api_url, params=params)
    try:
        data = resp.json()
    except Exception as e:
        return JsonResponse({'error': '금융감독원 API 응답 오류', 'detail': str(e), 'raw': resp.text}, status=500)
    base_list = data['result']['baseList']
    option_list = data['result']['optionList']

    for base in base_list:
        product, created = CreditLoanProduct.objects.update_or_create(
            product_code=base['fin_prdt_cd'],
            defaults={
                'product_name': base.get('fin_prdt_nm'),
                'bank_name': base.get('kor_co_nm'),
                'crdt_prdt_type_nm': base.get('crdt_prdt_type_nm'),
                'dcls_month': base.get('dcls_month'),
                'raw_json': base,
            }
        )
        for option in option_list:
            if option['fin_prdt_cd'] == product.product_code:
                CreditLoanOption.objects.update_or_create(
                    product=product,
                    crdt_lend_rate_type_nm=option.get('crdt_lend_rate_type_nm'),
                    defaults={
                        'crdt_grad_avg': option.get('crdt_grad_avg') or None,
                    }
                )
    return JsonResponse({'status': 'ok', 'count': len(base_list)})

def credit_loan_product_list(request):
    result = []
    products = CreditLoanProduct.objects.all()
    for product in products:
        options = product.options.all().values(
            'crdt_lend_rate_type', 'crdt_lend_rate_type_nm',
            'crdt_grad_1', 'crdt_grad_4', 'crdt_grad_5',
            'crdt_grad_6', 'crdt_grad_10', 'crdt_grad_11',
            'crdt_grad_12', 'crdt_grad_13', 'crdt_grad_avg'
        )
        result.append({
            'product_code': product.product_code,
            'product_name': product.product_name,
            'bank_name': product.bank_name,
            'fin_co_no': product.fin_co_no,
            'join_way': product.join_way,
            'crdt_prdt_type': product.crdt_prdt_type,
            'crdt_prdt_type_nm': product.crdt_prdt_type_nm,
            'cb_name': product.cb_name,
            'dcls_month': product.dcls_month,
            'dcls_strt_day': product.dcls_strt_day,
            'dcls_end_day': product.dcls_end_day,
            'fin_co_subm_day': product.fin_co_subm_day,
            'options': list(options),
        })
    return JsonResponse(result, safe=False)



# Create your views here.
API_KEY=settings.FIN_KEY
deposit=f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
saving=f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

# 0. Data Save
@api_view(['GET'])
def save_products(request):
    response=requests.get(deposit).json()
    for li in response.get('result').get('baseList'):
        fin_prdt_cd=li.get('fin_prdt_cd')
        kor_co_nm=li.get('kor_co_nm')
        fin_prdt_nm=li.get('fin_prdt_nm')
        etc_note=li.get('etc_note')
        join_member=li.get('join_member')
        join_way=li.get('join_way')
        save_deposit={
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_member':join_member,
            'join_way':join_way,
        }
        serializers=DepositProductsSerializer(data=save_deposit)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            
    for opt in response.get('result').get('optionList'):
        fin_prdt_cd=opt.get('fin_prdt_cd')
        intr_rate_type_nm=opt.get('intr_rate_type_nm')
        intr_rate=opt.get('intr_rate')
        save_trm=int(opt.get('save_trm'))
        save_option={
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'save_trm':save_trm,
        }
        serializer=DepositOptionsSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=DepositProducts.objects.get(fin_prdt_cd=save_option.get('fin_prdt_cd')))
            
    response=requests.get(saving).json()
    for li in response.get('result').get('baseList'):
        fin_prdt_cd=li.get('fin_prdt_cd')
        kor_co_nm=li.get('kor_co_nm')
        fin_prdt_nm=li.get('fin_prdt_nm')
        join_member=li.get('join_member')
        join_way=li.get('join_way')
        spcl_cnd=li.get('spcl_cnd')
        save_deposit={
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
        }
        serializers=SavingProductsSerializer(data=save_deposit)
        if serializers.is_valid(raise_exception=True):
            serializers.save()

    for opt in response.get('result').get('optionList'):
        fin_prdt_cd=opt.get('fin_prdt_cd')
        intr_rate_type_nm=opt.get('intr_rate_type_nm')
        intr_rate=opt.get('intr_rate')
        save_trm=int(opt.get('save_trm'))
        save_option={
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'save_trm':save_trm,
        }
        serializer=SavingOptionsSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=SavingProducts.objects.get(fin_prdt_cd=save_option.get('fin_prdt_cd')))
    return Response({"message": "okay "})


# 1. Data View
@api_view(['GET'])
def deposit_products(request):
    product=DepositProducts.objects.all()
    serializer=DepositProductsSerializer(product,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_options(request):
    option=DepositOptions.objects.all()
    serializer=DepositOptionsSerializer(option,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_products(request):
    product=SavingProducts.objects.all()
    serializer=SavingProductsSerializer(product,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_options(request):
    option=SavingOptions.objects.all()
    serializer=SavingOptionsSerializer(option,many=True)
    return Response(serializer.data)

# 2. 상세 View
@api_view(['GET'])
def deposit_product_detail(request, pid):
    product=get_object_or_404(DepositProducts,id=pid)
    serializer=DepositProductsSerializer(product)
    return Response(serializer.data)
@api_view(['GET'])
def deposit_option_detail(request,pid):
    option=get_list_or_404(DepositOptions,id=pid)
    serializer=DepositOptionsSerializer(option,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def saving_product_detail(request,pid):
    product=get_object_or_404(SavingProducts,id=pid)
    serializer=SavingProductsSerializer(product)
    return Response(serializer.data)
@api_view(['GET'])
def saving_option_detail(request,pid):
    option=get_list_or_404(SavingOptions,id=pid)
    serializer=SavingOptionsSerializer(option,many=True)
    return Response(serializer.data)

# @csrf_exempt
# def recommend_products(request):
#     # 프론트에서 user_id를 보내는 경우 (POST/GET 모두 지원)
#     user_id = request.GET.get('user_id') or (json.loads(request.body).get('user_id') if request.body else None)
#     if not user_id:
#         return JsonResponse({'error': 'user_id가 필요합니다.'}, status=400)

#     # 1. 유저 프로필 불러오기
#     try:
#         user_profile = Profile.objects.get(user_id=user_id)
#     except Profile.DoesNotExist:
#         return JsonResponse({'error': '해당 유저의 프로필이 없습니다.'}, status=404)

#     # 2. 상품 정보 추출 (option - product 연결)
#     def extract_products():
#         result = []
#         # Loan
#         for opt in LoanOption.objects.all()[:30]:
#             prod = LoanProduct.objects.get(id=opt.product_id)
#             result.append({
#                 "type": "loan",
#                 "product_id": prod.id,
#                 "product_name": prod.product_name,
#                 "bank_name": prod.bank_name,
#                 "option_detail": str(opt),  # 필요 정보만 선택해서 넣어도 됨
#             })
#         # Pension
#         for opt in PensionOption.objects.all()[:30]:
#             prod = PensionProduct.objects.get(id=opt.product_id)
#             result.append({
#                 "type": "pension",
#                 "product_id": prod.id,
#                 "product_name": prod.product_name,
#                 "bank_name": prod.bank_name,
#                 "option_detail": str(opt),
#             })
#         # CreditLoan
#         for opt in CreditLoanOption.objects.all()[:30]:
#             prod = CreditLoanProduct.objects.get(id=opt.product_id)
#             result.append({
#                 "type": "credit_loan",
#                 "product_id": prod.id,
#                 "product_name": prod.product_name,
#                 "bank_name": prod.bank_name,
#                 "option_detail": str(opt),
#             })
#         # RentLoan
#         for opt in RentLoanOption.objects.all()[:30]:
#             prod = RentLoanProduct.objects.get(id=opt.product_id)
#             result.append({
#                 "type": "rent_loan",
#                 "product_id": prod.id,
#                 "product_name": prod.product_name,
#                 "bank_name": prod.bank_name,
#                 "option_detail": str(opt),
#             })
#         return result

#     products = extract_products()

#     # 3. 프롬프트 생성
#     prompt = f"""
#     [User Profile]
#     Age: {user_profile.age}
#     Gender: {user_profile.gender}
#     Risk Profile: {user_profile.risk_profile}
#     Liquid Assets: {user_profile.liquid_assets}
#     Annual Income: {user_profile.annual_income}

#     [Products]
#     {json.dumps(products, ensure_ascii=False)}

#     위의 사용자 프로필에 가장 잘 맞는 금융 상품 10개(이하)를 product_id, product_name, bank_name, type, 그리고 추천 이유와 함께 반드시 JSON 배열 형태로 추천해줘. 
#     기타 설명 없이 JSON 데이터만 반환해.
#     """

#     # 4. OpenAI API 요청
#     openai.api_key = settings.OPENAI_API_KEY
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a financial product recommendation assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=1500,
#         temperature=0.4
#     )
#     answer = response['choices'][0]['message']['content']

#     # 5. AI 결과를 JSON으로 파싱
#     try:
#         result = json.loads(answer)
#     except Exception:
#         result = {"error": "AI가 올바른 JSON을 반환하지 않았습니다.", "raw": answer}

#     return JsonResponse(result, safe=False)
