# user/urls.py
from django.urls import path
from .views import user_profile_view 

urlpatterns = [
    path('profile/me/', user_profile_view),
]
