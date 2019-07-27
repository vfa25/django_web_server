'''
技术点：
rest_framework提供 Serializer 和 ModelSerializer API，
类似django的API（Form和ModelForm），
均可自由定制字段
'''

from django.db.models import Q
from rest_framework import serializers

from .models import ComponentCategory, Component


class ComponentOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class CategoryOriginSerializerSecondary(serializers.ModelSerializer):
    class Meta:
        model = ComponentCategory
        fields = '__all__'


class CategorySerializerSecondary(CategoryOriginSerializerSecondary):
    def to_representation(self, obj):
        result_json = super().to_representation(obj)
        if self.context and self.context['request']:
            search = self.context['request'].query_params.get('search', '')
            category = ComponentCategory.objects.get(id=result_json['id'])
            components = category.component_set.filter(
                Q(name__icontains=search) | Q(component_brief__icontains=search))
            result_json['children'] = ComponentOriginSerializer(
                components, many=True).data
        return result_json


class CategorySerializerPrimary(serializers.ModelSerializer):
    children = CategoryOriginSerializerSecondary(many=True)

    class Meta:
        model = ComponentCategory
        fields = '__all__'


class ComponentSerializer(CategoryOriginSerializerSecondary):
    category = CategorySerializerSecondary()
