

# 独立引入django的model

import os
import sys

# 指定根目录及配置
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"/../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoServer.settings")

import django
django.setup()

from data.category_data import row_data
from antd_cmp.models import ComponentCategory
from utils.common import get_md5


hashMap = {}

for item in row_data:
    hash_key_primary = get_md5(item['primary_title'])
    print(hash_key_primary)
    hash_key_secondary = get_md5(
        item['secondary_title'] + item['secondary_key'])

    if hash_key_primary in hashMap:
        primary_instance = hashMap[hash_key_primary]
    else:
        primary_instance = ComponentCategory()
        primary_instance.desc = item['primary_title']
        primary_instance.category_type = 1
        hashMap[hash_key_primary] = primary_instance
        primary_instance.save()

    if hash_key_secondary in hashMap:
        secondary_instance = hashMap[hash_key_secondary]
    else:
        secondary_instance = ComponentCategory()
        secondary_instance.name = item['secondary_name']
        secondary_instance.desc = item['secondary_title']
        secondary_instance.key = item['secondary_key']

        secondary_instance.category_type = 2
        hashMap[hash_key_secondary] = secondary_instance
        secondary_instance.parent_category = primary_instance
        secondary_instance.save()
