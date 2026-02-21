from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import timedelta
from django.utils import timezone


class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    referral_code = models.CharField(max_length=20, null=True, blank=True)

    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expiry = models.DateTimeField(null=True, blank=True)

    def generate_otp(self):
        self.otp = str(uuid.uuid4().int)[:6]
        self.otp_expiry = timezone.now() + timedelta(minutes=5)
        self.save()
