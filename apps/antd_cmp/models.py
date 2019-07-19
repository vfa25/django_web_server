'''
业务点：
以官网Component的左侧一级tab栏为一级类，左侧二级tab为二级类，内容区组件分类为三级类

技术点：
1. 父类外键指向自己：models.ForeignKey('self'。。。）
'''

from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class ComponentCategory(models.Model):
    '''
    类目类别
    '''
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(
        default='', max_length=30, verbose_name='类别名', help_text='类别名')
    code = models.CharField(
        default='', max_length=30, verbose_name='类别code', help_text='类别code')
    desc = models.TextField(
        default='', verbose_name='类别描述', help_text='类别描述')
    category_type = models.IntegerField(
        choices=CATEGORY_TYPE, verbose_name='类目级别', help_text='类目级别')
    parent_category = models.ForeignKey(
        'self', null=True, blank=True, verbose_name='父类目级别', help_text='父目录',
        related_name='children')
    is_nav = models.BooleanField(
        default=False, verbose_name='是否导航', help_text='是否导航')
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '组件类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ComponentCategoryTab(models.Model):
    '''
    组件类目下 -> Antd和Element的tab分类
    '''
    category = models.ForeignKey(
        ComponentCategory, related_name='tabs', verbose_name='组件类别')
    name = models.CharField(
        default='', max_length=30, verbose_name='tab名', help_text='tab名')
    desc = models.TextField(
        default='', max_length=200, verbose_name='tab描述', help_text='tab描述')
    image = models.ImageField(
        max_length=200, upload_to='tabs/')
    add_time = models.DateTimeField(
        default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = 'tab分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Component(models.Model):
    '''
    组件
    '''
    category = models.ForeignKey(ComponentCategory, verbose_name='组件类别')
    component_code = models.CharField(
        max_length=50, default='', verbose_name='组件唯一编号')
    name = models.CharField(max_length=100, verbose_name='组件名')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    fav_num = models.IntegerField(default=0, verbose_name='点赞数')
    collect_num = models.IntegerField(default=0, verbose_name='收藏数')
    easy_to_use = models.FloatField(default=0.0, verbose_name='易用指数')

    component_brief = models.TextField(max_length=500, verbose_name='描述')
    component_desc = UEditorField(
        verbose_name='内容', imagePath='component/images/', width=1000,
        height=300, filePath='component/files/', default='')
    component_front_image = models.ImageField(
        upload_to='component/images/', null=True, blank=True,
        verbose_name='封面图')
    is_new = models.BooleanField(default=False, verbose_name='是否新上')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '组件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ComponentImage(models.Model):
    """
    组件图片
    """
    component = models.ForeignKey(
        Component, verbose_name="组件", related_name="images")
    image = models.ImageField(
        upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '组件图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.component.name
