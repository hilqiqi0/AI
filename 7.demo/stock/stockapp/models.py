#-*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

SEX_CHOICES = (
    ('0','男'),
    ('1','女'),
)

class User(AbstractUser):
    gender = models.CharField(choices = SEX_CHOICES,max_length = 1,verbose_name = '性别')
    age = models.IntegerField(blank=True, null=True,verbose_name='年龄')
    profession = models.CharField(max_length = 128,verbose_name='职业')
    #可以为空
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    #不能重复
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    money = models.FloatField(blank=True, null=True, unique=True, verbose_name='资金')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

class Deal(models.Model):
    genre = models.BooleanField(default = True ,verbose_name = '买卖类型')
    number = models.IntegerField(verbose_name = '股票编码')
    amount = models.IntegerField(default = 100,verbose_name = '买卖数量')
    figure = models.FloatField(verbose_name = '成交金额')
    time = models.DateTimeField(auto_now_add=True,verbose_name = '交易时间')
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = '交易记录'
        verbose_name_plural = verbose_name
        ordering = ['-time']

    def __str__(self):
        return str(self.time)

class Hold(models.Model):
    number = models.IntegerField(verbose_name = '股票编码')
    amount = models.IntegerField(default = 100,verbose_name = '持有数量')
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = '持仓信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return str(self.number)

class Stock(models.Model):
    number = models.IntegerField(verbose_name= '股票编码')
    company_name = models.CharField(max_length = 64,verbose_name='公司名称')
    flow_in = models.FloatField(verbose_name = '总流入')
    flow_out = models.FloatField(verbose_name= '总流出')
    impressum = models.TextField(verbose_name='公司介绍')
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name = '股票信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.company_name


class Link(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    callback_url = models.URLField(verbose_name='url地址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title 