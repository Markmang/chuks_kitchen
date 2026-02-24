from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from .models import User
from django.utils import timezone


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": "User created. OTP sent.",
                    "user_id": user.id,
                    "otp_for_testing": user.otp
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        if user.otp != otp:
            return Response({"error": "Invalid OTP"}, status=400)

        if timezone.now() > user.otp_expiry:
            return Response({"error": "OTP expired"}, status=400)

        user.is_verified = True
        user.save()

        return Response({"message": "Account verified"})

