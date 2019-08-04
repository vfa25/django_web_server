# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-28 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antd_cmp', '0003_auto_20190721_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentcategory',
            name='category_type',
            field=models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目')], help_text='类目级别', verbose_name='类目级别'),
        ),
    ]
