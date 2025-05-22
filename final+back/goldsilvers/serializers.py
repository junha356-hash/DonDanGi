from rest_framework import serializers
from .models import GoldPrice, SilverPrice

class GoldPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldPrice
        fields = ['date', 'Close/Last']

class SilverPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilverPrice
        fields = ['date', 'Close/Last']
