'''
文档参考
https://django-filter.readthedocs.io/en/master/guide/rest_framework.html
'''

from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Component


class ComponentFilter(filters.FilterSet):
    '''
    过滤类
    '''
    hardNumMin = filters.NumberFilter(
        field_name='easy_to_use', lookup_expr='gte')
    hardNumMax = filters.NumberFilter(
        field_name='easy_to_use', lookup_expr='lte')
    # name = filters.CharFilter(
    #     field_name='name', lookup_expr='contains')
    cmpCategory = filters.NumberFilter(method='cmp_category_filter')

    def cmp_category_filter(self, queryset, name, value):
        return queryset.filter(
            Q(category_id=value) | Q(category__parent_category_id=value))

    class Meta:
        model = Component
        fields = ['hardNumMin', 'hardNumMax']
