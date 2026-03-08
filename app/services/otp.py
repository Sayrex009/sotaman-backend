import random
import time
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from app.models import EmailOTP

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    send_mail(
        "Verification Code",
        f"Your verification code is: {otp}",
        "yourgmail@gmail.com",
        [email],
    )

def save_otp(email, otp):
    EmailOTP.objects.create(email=email, code=otp, created_at=timezone.now())

def verify_otp(email, otp, expire_minutes=5):
    otp_obj = EmailOTP.objects.filter(
        email=email,
        code=otp,
        created_at__gte=timezone.now() - timedelta(minutes=expire_minutes)
    ).first()
    
    if otp_obj:
        otp_obj.delete() 
        return True
    return False
