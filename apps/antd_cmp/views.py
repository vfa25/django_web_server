'''
技术点：
    这里其实已经在根url注册了路由，故直接使用 mixins的ModelMixin，而不是 generics的APIView
    queryset是GenericAPIView的api
    如果不使用过滤器，就需手动实现get_queryset方法，后者在mixins.ListModelMixin源码里一看便知
'''

from django.db.models import Q
from rest_framework.response import Response
# https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ComponentFilter

from .models import ComponentCategory, Component
from .serializers import (
    CategorySerializerPrimary, ComponentSerializer, CategorySerializerSecondary)


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        组件分类列表数据
    '''
    queryset = ComponentCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializerPrimary
    # authentication_classes = (TokenAuthentication,)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ComponentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class ComponentListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    组件列表页：序列化、分页、辅助API调试、过滤、搜索、排序
    '''
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    pagination_class = ComponentPagination
    filter_backends = (
        DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ComponentFilter
    search_fields = ('name', 'component_brief')
    ordering_fields = ('easy_to_use', 'add_time')
    ordering = ['-add_time']

class SearchCagetoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializerSecondary

    def get_queryset(self):
        search = self.request.query_params.get('search', '')
        if not search:
            return ComponentCategory.objects.none()
        components = Component.objects.filter(
            Q(name__icontains=search) | Q(component_brief__icontains=search))
        return [component.category for component in components]
