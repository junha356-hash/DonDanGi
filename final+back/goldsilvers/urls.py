from django.urls import path
from . import views

urlpatterns = [
    path('gold-prices/', views.gold_prices),
    path('silver-prices/', views.silver_prices),
]
