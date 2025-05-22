# user/serializers.py

from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['age', 'gender', 'risk_profile', 'liquid_assets', 'annual_income', 'image', 'username',]
