"""djangoServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from django.conf.urls import url, include
# from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
# from django.urls import path
import xadmin
from djangoServer.settings import MEDIA_ROOT

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter


from antd_cmp.views import (
    CategoryViewset, SearchCagetoryViewset)
from users.views import (
    SmsCodeViewset, MobileRegisterViewset)

# create a router and register out viewsets with it
router = DefaultRouter(trailing_slash=False)

# category的url
router.register(r'categorys', CategoryViewset, base_name='categorys')
router.register(r'search', SearchCagetoryViewset, base_name='search')
router.register(r'smscode', SmsCodeViewset, base_name='smscode')
router.register(r'register/mobile', MobileRegisterViewset,
                base_name='mobileRegister')


# xadmin 首次登陆，创建超级用户 python manage.py createsuperuser
urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # https://www.django-rest-framework.org/topics/documenting-your-api/#documenting-your-api
    url('^docs/', include_docs_urls(title='API文档')),

    # https://www.django-rest-framework.org/#installation
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers
    url('', include(router.urls)),

    # https://www.django-rest-framework.org/api-guide/authentication/#by-exposing-an-api-endpoint
    # url(r'^api-token-auth/', views.obtain_auth_token)

    # http://jpadilla.github.io/django-rest-framework-jwt/
    url(r'^login$', obtain_jwt_token)
]
