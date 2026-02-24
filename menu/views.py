from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer


class FoodListCreateView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
