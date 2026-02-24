from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, Order
from decimal import Decimal
from rest_framework.generics import RetrieveAPIView
from .serializers import OrderSerializer


class CreateOrderView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")

        if not user_id:
            return Response(
                {"error": "user_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found for this user"},
                status=status.HTTP_404_NOT_FOUND
            )

        if not cart.items.exists():
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        total = Decimal("0.00")

        for item in cart.items.all():
            if not item.food.available:
                return Response(
                    {"error": f"{item.food.name} unavailable"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            total += item.food.price * item.quantity

        order = Order.objects.create(
            user_id=user_id,
            total_price=total
        )

        cart.items.all().delete()

        return Response(
            {
                "message": "Order created successfully",
                "order_id": order.id,
                "total_price": str(total)
            },
            status=status.HTTP_201_CREATED
        )
    
class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer