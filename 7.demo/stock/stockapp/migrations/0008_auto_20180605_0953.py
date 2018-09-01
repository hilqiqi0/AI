# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0007_auto_20180201_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='amount',
            field=models.IntegerField(verbose_name='买卖数量', default=100),
        ),
        migrations.AlterField(
            model_name='deal',
            name='figure',
            field=models.FloatField(verbose_name='成交金额'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='genre',
            field=models.BooleanField(verbose_name='买卖类型', default=True),
        ),
        migrations.AlterField(
            model_name='deal',
            name='number',
            field=models.IntegerField(verbose_name='股票编码'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='time',
            field=models.DateTimeField(verbose_name='交易时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hold',
            name='amount',
            field=models.IntegerField(verbose_name='持有数量', default=100),
        ),
        migrations.AlterField(
            model_name='hold',
            name='number',
            field=models.IntegerField(verbose_name='股票编码'),
        ),
        migrations.AlterField(
            model_name='link',
            name='callback_url',
            field=models.URLField(verbose_name='url地址'),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=50),
        ),
        migrations.AlterField(
            model_name='stock',
            name='company_name',
            field=models.CharField(verbose_name='公司名称', max_length=64),
        ),
        migrations.AlterField(
            model_name='stock',
            name='flow_in',
            field=models.FloatField(verbose_name='总流入'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='flow_out',
            field=models.FloatField(verbose_name='总流出'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='impressum',
            field=models.TextField(verbose_name='公司介绍'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='number',
            field=models.IntegerField(verbose_name='股票编码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, verbose_name='年龄', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('0', '男'), ('1', '女')], verbose_name='性别', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, verbose_name='手机号码', max_length=11, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.FloatField(blank=True, verbose_name='资金', unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(verbose_name='职业', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(blank=True, verbose_name='QQ号码', max_length=20, null=True),
        ),
    ]
