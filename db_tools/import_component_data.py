

# 独立引入django的model

import os
import sys

# 指定根目录及配置
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoServer.settings')

import django
django.setup()

from data.component_data import row_data
from antd_cmp.models import ComponentCategory, Component
from utils.common import get_md5


for component_detail in row_data:
    component = Component()
    component.name = component_detail['name']
    component.easy_to_use = int(component_detail['easy_to_use'])
    component.component_brief = (
        component_detail['desc'] if component_detail['desc'] is not None else '')
    category_name = component_detail['category_name']
    category = ComponentCategory.objects.filter(name=category_name)
    if category:
        component.category = category[0]
    component.save()
