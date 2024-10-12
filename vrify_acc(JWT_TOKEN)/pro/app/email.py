from django.core.mail import send_mail
from django.conf import settings
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

def send_verification_email(email):
    try:
        subject = 'Account Verification'
        user = User.objects.get(email=email)
        print("email: ", email)
        token = RefreshToken.for_user(user).access_token
        print("token: ",token)

        verification_link = f"http://127.0.0.1:8000/?token={token}"

        #Email message
        message = f'Click the link below to verify your account\n{verification_link}'
        email_from = settings.DEFAULT_FROM_EMAIL
        send_mail(subject,message,email_from,[email])
        return True

    except Exception as e:
        print(f"Error sending verification email to {email}:{e}")
        return False        