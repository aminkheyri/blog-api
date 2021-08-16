from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import SendSms, VerifyOtp

app_name = 'accounts'
urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/send_sms/', SendSms.as_view(), name='send_sms'),
    path('api/verify_otp/', VerifyOtp.as_view(), name='verify_otp'),

]
