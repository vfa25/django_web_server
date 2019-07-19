'''
技术点：
    这里其实已经在根url注册了路由，故直接使用 mixins的ModelMixin，而不是 generics的APIView
    queryset是GenericAPIView的api
    如果不使用过滤器，就需手动实现get_queryset方法，后者在mixins.ListModelMixin源码里一看便知
'''

from rest_framework.response import Response
# https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import ComponentCategory
from .serializers import (CategorySerializerPrimary, CategorySerializerSecondary)


class CategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    list:
        组件分类列表数据
    '''
    queryset = ComponentCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializerPrimary


class CategoryBlockViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    '''
    list:
        左侧路由下Block列表数据
    '''
    queryset = ComponentCategory.objects.filter(category_type=2)
    serializer_class = CategorySerializerSecondary
