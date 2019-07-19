import xadmin

from .models import RewardOrderInfo


class OrderInfoAdmin(object):
    list_display = ['user', 'component', 'order_sn',  'trade_no', 'pay_status',
                    'post_script', 'order_mount', 'pay_time', 'add_time']


xadmin.site.register(RewardOrderInfo, OrderInfoAdmin)
