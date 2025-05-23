# finance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 연금저축 
    # path('fetch-pension-products/', views.fetch_pension_products, name='fetch_pension_products'),
    # path('pension-products/', views.pension_product_list, name='pension_product_list'),
    # 주택담보대출
    path('fetch-loan-products/', views.fetch_loan_products, name='fetch_loan_products'),
    path('products/', views.loan_product_list, name='loan_product_list'),
    # 전세자금대출
    path('fetch-rent-loan-products/', views.fetch_rent_loan_products, name='fetch_rent_loan_products'),
    path('rent-loan-products/', views.rent_loan_product_list, name='rent_loan_product_list'),
    # 개인신용대출
    path('fetch-credit-loan-products/', views.fetch_credit_loan_products, name='fetch_credit_loan_products'),
    path('credit-loan-products/', views.credit_loan_product_list, name='credit_loan_product_list'),
]
