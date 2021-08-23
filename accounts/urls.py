from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .api_views import SendSms, VerifyOtp

app_name = 'accounts'
urlpatterns = [

    path('api/api-token-auth/', obtain_jwt_token, name='api_token_auth'),
    path('api/api-token-refresh/', refresh_jwt_token, name='token_refresh'),
    path('api/send_sms/', SendSms.as_view(), name='send_sms'),
    path('api/verify_otp/', VerifyOtp.as_view(), name='verify_otp'),

]
