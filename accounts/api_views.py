from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserSerializer, PhoneNumberSerializer, RandomCodeSerializer
from djangoProject.permissions import IsSuperUser
from rest_framework.views import APIView
from random import randint
from kavenegar import *
from django.http import HttpResponse
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]


phone_dict = {}


class SendSms(APIView):
    def post(self, request):
        serialized_data = PhoneNumberSerializer(data=request.data)
        if serialized_data.is_valid():
            rand_int = randint(10000, 99999)
            phone_number = serialized_data.data.get('phone')

            phone_dict[str(phone_number)] = rand_int

            # Sending Sms by kavenegar
            api = KavenegarAPI(
                '584D34694977644E474C64776950746533335A524B624F4A77644B314A56766956736366593077693972593D')
            params = {'sender': '10008663', 'receptor': phone_number, 'message': str(rand_int)}
            api.sms_send(params)
            return Response({"message": "sent"})
        return Response({"message": "failed"})


class VerifyOtp(APIView):
    def post(self, request):
        serialized_data = RandomCodeSerializer(data=request.data)

        if serialized_data.is_valid():

            random_code = serialized_data.data.get('random_code')
            phone = serialized_data.data.get('phone')

            if random_code == phone_dict[phone]:
                pass
                # creating a jwt token manually
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(request.user)
                token = jwt_encode_handler(payload)
                return HttpResponse('Get token auth request and data is as: {}'.format(token))

        return Response({'error': 'invalid code'})
