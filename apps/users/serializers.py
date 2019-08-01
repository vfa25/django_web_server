
import re
from django.db.models import Q
from datetime import (datetime, timedelta)
from rest_framework import serializers
from django.contrib.auth import get_user_model
from djangoServer.settings import REGEX_MOBILE
from rest_framework.validators import UniqueValidator

from .models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        '''
        验证手机号码
        '''
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')

        # 手机号合法校验
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(
            hours=0, minutes=1, seconds=0)

        if VerifyCode.objects.filter(
                add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError('60秒后可重新获取短信验证码')

        return mobile


class MobileRegisterSerializer(serializers.ModelSerializer):
    '''
    校验 短信验证码 和 手机号，可以自定义校验字段，并在 validate 做 自定义操作
    '''
    smscode = serializers.CharField(
        required=True, min_length=6, max_length=6, help_text='短信验证码',
        write_only=True, label="短信验证码",
        error_messages={
            'blank': '短信验证码不能为空',
            'required': '短信验证码不能为空',
            'max_length': '请输入6位数的短信验证码',
            'min_length': '请输入6位数的短信验证码'
        })
    mobile = serializers.CharField(
        required=True, allow_blank=False, label='电话号码',
        validators=[UniqueValidator(queryset=User.objects.all(), message='用户已存在')])
    password = serializers.CharField(
        style={'input_type': 'password'}, label='密码', write_only=True
    )
    username = serializers.CharField(
        required=False, allow_blank=True, read_only=True
    )

    def validate_smscode(self, code):
        verify_records = VerifyCode.objects.filter(
            mobile=self.initial_data['mobile']).order_by('-add_time')
        if verify_records:
            last_records = verify_records[0]

            five_mintes_ago = datetime.now() - timedelta(
                hours=0, minutes=15, seconds=0)
            if five_mintes_ago > last_records.add_time:
                raise serializers.ValidationError('验证码过期')

            if last_records.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        attrs['username'] = attrs['mobile']
        del attrs['smscode']
        return attrs

    class Meta:
        model = User
        fields = ('smscode', 'username', 'mobile', 'password')
