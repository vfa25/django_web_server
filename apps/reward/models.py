from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from antd_cmp.models import Component
User = get_user_model()


class RewardOrderInfo(models.Model):
    '''
    打赏订单
    '''
    ORDER_STATUS = (
        ('TRADE_SUCCESS', '成功'),
        ('TRADE_CLOSED', '超时关闭'),
        ('WAIT_BUYER_PAY', '交易创建'),
        ('TRADE_FINISHED', '交易结束'),
        ('paying', '待支付'),
    )

    user = models.ForeignKey(User, verbose_name='用户')
    component = models.ForeignKey(Component, verbose_name='组件')
    order_sn = models.CharField(
        max_length=30, null=True, blank=True, unique=True, verbose_name='订单号')
    trade_no = models.CharField(
        max_length=100, unique=True, null=True, blank=True, verbose_name='交易号')
    pay_status = models.CharField(
        choices=ORDER_STATUS, default='paying', max_length=30,
        verbose_name='订单状态')
    post_script = models.CharField(max_length=200, verbose_name='订单留言')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '打赏订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)
