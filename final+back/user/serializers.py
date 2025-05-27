# user/serializers.py

from rest_framework import serializers
from .models import Profile
from products.serializers import DepositProductsSerializer, SavingProductsSerializer

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    my_deposits = DepositProductsSerializer(many=True, read_only=True)
    my_savings = SavingProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'age', 
            'gender', 
            'risk_profile', 
            'liquid_assets', 
            'annual_income', 
            'image', 
            'username',
            'my_deposits',
            'my_savings',
            ]
