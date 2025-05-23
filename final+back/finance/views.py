# finance/views.py 일부 예시
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import LoanProduct, LoanOption, RentLoanProduct, RentLoanOption, CreditLoanProduct, CreditLoanOption
from django.views.decorators.csrf import csrf_exempt

# 연금저축 
# @csrf_exempt
# def fetch_pension_products(request):
#     api_url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
#     api_key = settings.FSS_API_KEY
#     params = {
#         'auth': api_key,
#         'topFinGrpNo': '020000',  # 은행 (필요에 따라 조정)
#         'pageNo': 1
#     }
#     resp = requests.get(api_url, params=params)
#     data = resp.json()
#     base_list = data['result']['baseList']
#     option_list = data['result']['optionList']

#     for base in base_list:
#         product, created = PensionProduct.objects.update_or_create(
#             product_code=base['fin_prdt_cd'],
#             defaults={
#                 'product_name': base.get('fin_prdt_nm'),
#                 'bank_name': base.get('kor_co_nm'),
#                 'fin_co_no': base.get('fin_co_no'),
#                 'join_way': base.get('join_way'),
#                 'pnsn_kind': base.get('pnsn_kind'),
#                 'pnsn_kind_nm': base.get('pnsn_kind_nm'),
#                 'sale_strt_day': base.get('sale_strt_day'),
#                 'mntn_cnt': base.get('mntn_cnt'),
#                 'prdt_type': base.get('prdt_type'),
#                 'prdt_type_nm': base.get('prdt_type_nm'),
#                 'dcls_rate': base.get('dcls_rate') or None,
#                 'guar_rate': base.get('guar_rate') or None,
#                 'btrm_prft_rate_1': base.get('btrm_prft_rate_1') or None,
#                 'btrm_prft_rate_2': base.get('btrm_prft_rate_2') or None,
#                 'btrm_prft_rate_3': base.get('btrm_prft_rate_3') or None,
#                 'etc': base.get('etc'),
#                 'sale_co': base.get('sale_co'),
#                 'dcls_month': base.get('dcls_month'),
#                 'dcls_strt_day': base.get('dcls_strt_day'),
#                 'dcls_end_day': base.get('dcls_end_day'),
#                 'fin_co_subm_day': base.get('fin_co_subm_day'),
#                 'raw_json': base,
#             }
#         )
#         for option in option_list:
#             if option['fin_prdt_cd'] == product.product_code:
#                 PensionOption.objects.update_or_create(
#                     product=product,
#                     intr_rate_type=option.get('intr_rate_type'),
#                     intr_rate_type_nm=option.get('intr_rate_type_nm'),
#                     rsrv_type=option.get('rsrv_type'),
#                     rsrv_type_nm=option.get('rsrv_type_nm'),
#                     save_trm=option.get('save_trm'),
#                     defaults={
#                         'intr_rate': option.get('intr_rate') or None,
#                         'intr_rate2': option.get('intr_rate2') or None,
#                     }
#                 )
#     return JsonResponse({'status': 'ok', 'count': len(base_list)})

# def pension_product_list(request):
#     result = []
#     products = PensionProduct.objects.all()
#     for product in products:
#         options = product.options.all().values(
#             'intr_rate_type', 'intr_rate_type_nm',
#             'rsrv_type', 'rsrv_type_nm',
#             'save_trm', 'intr_rate', 'intr_rate2'
#         )
#         result.append({
#             'product_code': product.product_code,
#             'product_name': product.product_name,
#             'bank_name': product.bank_name,
#             'fin_co_no': product.fin_co_no,
#             'join_way': product.join_way,
#             'pnsn_kind': product.pnsn_kind,
#             'pnsn_kind_nm': product.pnsn_kind_nm,
#             'sale_strt_day': product.sale_strt_day,
#             'mntn_cnt': product.mntn_cnt,
#             'prdt_type': product.prdt_type,
#             'prdt_type_nm': product.prdt_type_nm,
#             'dcls_rate': product.dcls_rate,
#             'guar_rate': product.guar_rate,
#             'btrm_prft_rate_1': product.btrm_prft_rate_1,
#             'btrm_prft_rate_2': product.btrm_prft_rate_2,
#             'btrm_prft_rate_3': product.btrm_prft_rate_3,
#             'etc': product.etc,
#             'sale_co': product.sale_co,
#             'dcls_month': product.dcls_month,
#             'dcls_strt_day': product.dcls_strt_day,
#             'dcls_end_day': product.dcls_end_day,
#             'fin_co_subm_day': product.fin_co_subm_day,
#             'options': list(options),
#         })
#     return JsonResponse(result, safe=False)

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
                'join_way': base.get('join_way'),
                'loan_inci_expn': base.get('loan_inci_expn'),
                'erly_rpay_fee': base.get('erly_rpay_fee'),
                'dly_rate': base.get('dly_rate'),
                'loan_lmt': base.get('loan_lmt'),
                'dcls_month': base.get('dcls_month'),
                'dcls_strt_day': base.get('dcls_strt_day'),
                'dcls_end_day': base.get('dcls_end_day'),
                'fin_co_subm_day': base.get('fin_co_subm_day'),
                'raw_json': base,
            }
        )
        # 2. optionList(옵션) 저장
        for option in option_list:
            # 옵션이 현재 상품 코드와 동일한 것만 연결
            if option['fin_prdt_cd'] == product.product_code:
                LoanOption.objects.update_or_create(
                    product=product,
                    mrtg_type=option.get('mrtg_type'),
                    mrtg_type_nm=option.get('mrtg_type_nm'),
                    rpay_type=option.get('rpay_type'),
                    rpay_type_nm=option.get('rpay_type_nm'),
                    lend_rate_type=option.get('lend_rate_type'),
                    lend_rate_type_nm=option.get('lend_rate_type_nm'),
                    defaults={
                        'lend_rate_min': option.get('lend_rate_min') or None,
                        'lend_rate_max': option.get('lend_rate_max') or None,
                        'lend_rate_avg': option.get('lend_rate_avg') or None,
                    }
                )
    return JsonResponse({'status': 'ok', 'count': len(base_list)})

# 전세자금대출 
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
                'fin_co_no': base.get('fin_co_no'),
                'join_way': base.get('join_way'),
                'loan_inci_expn': base.get('loan_inci_expn'),
                'erly_rpay_fee': base.get('erly_rpay_fee'),
                'dly_rate': base.get('dly_rate'),
                'loan_lmt': base.get('loan_lmt'),
                'dcls_month': base.get('dcls_month'),
                'dcls_strt_day': base.get('dcls_strt_day'),
                'dcls_end_day': base.get('dcls_end_day'),
                'fin_co_subm_day': base.get('fin_co_subm_day'),
                'raw_json': base,
            }
        )
        for option in option_list:
            if option['fin_prdt_cd'] == product.product_code:
                RentLoanOption.objects.update_or_create(
                    product=product,
                    rpay_type=option.get('rpay_type'),
                    rpay_type_nm=option.get('rpay_type_nm'),
                    lend_rate_type=option.get('lend_rate_type'),
                    lend_rate_type_nm=option.get('lend_rate_type_nm'),
                    defaults={
                        'lend_rate_min': option.get('lend_rate_min') or None,
                        'lend_rate_max': option.get('lend_rate_max') or None,
                        'lend_rate_avg': option.get('lend_rate_avg') or None,
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
                'fin_co_no': base.get('fin_co_no'),
                'join_way': base.get('join_way'),
                'crdt_prdt_type': base.get('crdt_prdt_type'),
                'crdt_prdt_type_nm': base.get('crdt_prdt_type_nm'),
                'cb_name': base.get('cb_name'),
                'dcls_month': base.get('dcls_month'),
                'dcls_strt_day': base.get('dcls_strt_day'),
                'dcls_end_day': base.get('dcls_end_day'),
                'fin_co_subm_day': base.get('fin_co_subm_day'),
                'raw_json': base,
            }
        )
        for option in option_list:
            if option['fin_prdt_cd'] == product.product_code:
                CreditLoanOption.objects.update_or_create(
                    product=product,
                    crdt_lend_rate_type=option.get('crdt_lend_rate_type'),
                    crdt_lend_rate_type_nm=option.get('crdt_lend_rate_type_nm'),
                    defaults={
                        'crdt_grad_1': option.get('crdt_grad_1') or None,
                        'crdt_grad_4': option.get('crdt_grad_4') or None,
                        'crdt_grad_5': option.get('crdt_grad_5') or None,
                        'crdt_grad_6': option.get('crdt_grad_6') or None,
                        'crdt_grad_10': option.get('crdt_grad_10') or None,
                        'crdt_grad_11': option.get('crdt_grad_11') or None,
                        'crdt_grad_12': option.get('crdt_grad_12') or None,
                        'crdt_grad_13': option.get('crdt_grad_13') or None,
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