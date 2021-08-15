from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .api_views import GenerateOtp, VerifyOtp

app_name = 'accounts'
urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/generate_otp/', GenerateOtp.as_view(), name='generate_otp'),
    # path('api/verify_otp/', VerifyOtp.as_view(), name='verify_otp'),

]
