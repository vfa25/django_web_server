import xadmin

from .models import UserFav, UserCollect, UserLeavingMessage


class UserFavAdmin(object):
    list_display = ['user', 'component', 'add_time']


class UserCollectAdmin(object):
    list_display = ['user', 'component', 'add_time']


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', 'message', 'add_time']


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserCollect, UserCollectAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
