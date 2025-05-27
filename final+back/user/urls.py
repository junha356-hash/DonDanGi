# user/urls.py
from django.urls import path
from .views import user_profile_view 
from .views import UserProductAPIView

urlpatterns = [
    path('profile/me/', user_profile_view),
    path('products/', UserProductAPIView.as_view()),
]
