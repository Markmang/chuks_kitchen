from django.urls import path
from .views import CreateOrderView, OrderDetailView


urlpatterns = [
     path("orders", CreateOrderView.as_view(), name="create-order"),
     path("orders/<int:pk>", OrderDetailView.as_view(), name="order-detail"),
]
   