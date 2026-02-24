from django.urls import path
from .views import FoodListCreateView

urlpatterns = [
    path("foods", FoodListCreateView.as_view(), name="foods"),
]