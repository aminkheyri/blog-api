from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserSerializer
from djangoProject.permissions import IsSuperUser
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from random import randint
from kavenegar import *
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework_jwt.settings import api_settings


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]


class GetPhoneAndCode():
    def __init__(self, phone):
        self.rand_num = None
        self.phone = get_object_or_404(User, phone=phone)


class SendSms(APIView, GetPhoneAndCode):
    def post(self, request):
        if self.phone:
            self.rand_num = randint(100, 10000)
            # Sending Sms by kavenegar
            api = KavenegarAPI(
                '584D34694977644E474C64776950746533335A524B624F4A77644B314A56766956736366593077693972593D')
            params = {'sender': 'amin', 'receptor': self.phone, 'message': self.rand_num}
            api.sms_send(params)
            return HttpResponseRedirect(redirect_to='accounts:verify_otp')
        else:
            return 'phone number does not exists'


class VerifyOtp(APIView, GetPhoneAndCode):
    def post(self, request):
        code = request.data.get('code', None)
        if code == self.rand_num:
            # creating a jwt token manually
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(request.id)
            token = jwt_encode_handler(payload)
            return HttpResponse('Get token auth request and data is as: {}'.format(token))
        else:
            return 'your code is wrong'
