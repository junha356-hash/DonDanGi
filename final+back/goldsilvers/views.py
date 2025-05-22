from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GoldPrice, SilverPrice
from .serializers import GoldPriceSerializer, SilverPriceSerializer

@api_view(['GET'])
def gold_prices(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    queryset = GoldPrice.objects.all()
    if start and end:
        queryset = queryset.filter(date__range=[start, end])
    serializer = GoldPriceSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def silver_prices(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    queryset = SilverPrice.objects.all()
    if start and end:
        queryset = queryset.filter(date__range=[start, end])
    serializer = SilverPriceSerializer(queryset, many=True)
    return Response(serializer.data)
