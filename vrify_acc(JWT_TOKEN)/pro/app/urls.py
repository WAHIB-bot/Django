from django.urls import path
from .views import RegisterApi,LoginApi,VerificationAccount
from app import views

urlpatterns = [
    path('send_email/', RegisterApi.as_view(), name='send_email'),
    path('verify/', VerificationAccount.as_view(), name='send_email'),
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('loginauth/', LoginApi.as_view(), name='signup'),
    # path('dahsboard', , name='send_email'),

]