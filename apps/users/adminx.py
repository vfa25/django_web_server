import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '后台管理系统'
    site_footer = '版权所有 转载随意'
    menu_style = 'accordion'


class VerifyCodeManage(object):
    list_display = ['code', 'mobile', 'email', "add_time"]

xadmin.site.register(VerifyCode, VerifyCodeManage)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
