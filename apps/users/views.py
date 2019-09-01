from random import choice

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from braces.views import CsrfExemptMixin

from djangoServer.settings import YUNPIAN_API_KEY
from .serializers import (
    SmsSerializer, MobileRegisterSerializer)
from .models import VerifyCode
from utils.yunpian import YunPian

User = get_user_model()

# Create your views here.	# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CsrfExemptMixin, CreateModelMixin, viewsets.GenericViewSet):
    '''
    发送短信验证码
    '''

    authentication_classes = []
    serializer_class = SmsSerializer

    def generate_code(self):
        '''
        生成六位数验证码
        '''
        seeds = '0123456789'
        random_str = [choice(seeds) for i in range(6)]
        return ''.join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']
        yunpian = YunPian(YUNPIAN_API_KEY)
        code = self.generate_code()
        sms_response = yunpian.single_send_sms(code=code, mobile=mobile)

        if sms_response['code'] != 0:
            return Response({
                'mobile': sms_response['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            headers = super().get_success_headers(serializer.data)
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile
            }, status=status.HTTP_201_CREATED, headers=headers)


class MobileRegisterViewset(CsrfExemptMixin, CreateModelMixin, viewsets.GenericViewSet):
    '''
    用户：重写create（辅助函数perform_create）以定制返回
    '''

    authentication_classes = []
    serializer_class = MobileRegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username
        del re_dict['username']

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
