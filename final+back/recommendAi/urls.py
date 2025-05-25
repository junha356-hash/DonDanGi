# recommendAi/urls.py
from django.urls import path
from .views import AIRecommendView  # <- 추천 API 뷰 import

urlpatterns = [
    path('recommend/ai/', AIRecommendView.as_view(), name='ai-recommend'),
    path('ai_product/', AIRecommendView.as_view()),
]
