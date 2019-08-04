# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-20 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('antd_cmp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentcategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='antd_cmp.ComponentCategory', verbose_name='父类目级别'),
        ),
    ]
