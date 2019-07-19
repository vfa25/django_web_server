from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birday = models.DateField(verbose_name='生日', blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=(('male', '男'), ('female', '女')),
        default='female')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, blank=True, null=True)
    image = models.ImageField(upload_to='image/%Y/%m',
                              default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
