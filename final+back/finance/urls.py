# finance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 주택담보대출
    path('fetch-loan-products/', views.fetch_loan_products, name='fetch_loan_products'),
    path('products/', views.loan_product_list, name='loan_product_list'),
    # 전세자금대출
    path('fetch-rent-loan-products/', views.fetch_rent_loan_products, name='fetch_rent_loan_products'),
    path('rent-loan-products/', views.rent_loan_product_list, name='rent_loan_product_list'),
    # 개인신용대출
    path('fetch-credit-loan-products/', views.fetch_credit_loan_products, name='fetch_credit_loan_products'),
    path('credit-loan-products/', views.credit_loan_product_list, name='credit_loan_product_list'),
    # 예금 및 적금 
    path('save-products/',views.save_products ),
    path('deposit_products/',views.deposit_products),
    path('deposit_options/',views.deposit_options),
    path('savings_products/',views.saving_products),
    path('savings_options/',views.saving_options),
]
