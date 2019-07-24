'''
技术点：
rest_framework提供 Serializer 和 ModelSerializer API，
类似django的API（Form和ModelForm），
均可自由定制字段
'''

from rest_framework import serializers

from .models import ComponentCategory, Component


class CategorySerializerSecondary(serializers.ModelSerializer):

    class Meta:
        model = ComponentCategory
        fields = '__all__'


class CategorySerializerPrimary(serializers.ModelSerializer):
    children = CategorySerializerSecondary(many=True)

    class Meta:
        model = ComponentCategory
        fields = '__all__'

class ComponentSerializer(serializers.ModelSerializer):
    category = CategorySerializerSecondary()

    class Meta:
        model = Component
        fields = '__all__'
