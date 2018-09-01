# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'}, unique=True, max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('gender', models.BooleanField(verbose_name='性别', default=True)),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('profession', models.CharField(verbose_name='职业', max_length=128)),
                ('qq', models.CharField(verbose_name='QQ号码', null=True, max_length=20, blank=True)),
                ('mobile', models.CharField(verbose_name='手机号码', null=True, max_length=11, unique=True, blank=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_query_name='user', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_name='user_set')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_query_name='user', to='auth.Permission', help_text='Specific permissions for this user.', blank=True, related_name='user_set')),
            ],
            options={
                'verbose_name': '用户信息',
                'ordering': ['-id'],
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.BooleanField(verbose_name='买卖类型', default=True)),
                ('number', models.IntegerField(verbose_name='股票编码')),
                ('amount', models.IntegerField(verbose_name='买卖数量', default=100)),
                ('figure', models.FloatField(verbose_name='成交金额')),
                ('time', models.DateTimeField(verbose_name='交易时间', default=datetime.datetime(2017, 11, 8, 16, 0, 52, 567597))),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '交易记录',
                'ordering': ['-time'],
                'verbose_name_plural': '交易记录',
            },
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name='股票编码')),
                ('amount', models.IntegerField(verbose_name='持有数量', default=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '持仓信息',
                'ordering': ['id'],
                'verbose_name_plural': '持仓信息',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('callback_url', models.URLField(verbose_name='url地址')),
            ],
            options={
                'verbose_name': '友情链接',
                'ordering': ['id'],
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name='股票编码')),
                ('company_name', models.CharField(verbose_name='公司名称', max_length=64)),
                ('flow_in', models.FloatField(verbose_name='总流入')),
                ('flow_out', models.FloatField(verbose_name='总流出')),
                ('impressum', models.TextField(verbose_name='公司介绍')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '股票信息',
                'ordering': ['id'],
                'verbose_name_plural': '股票信息',
            },
        ),
    ]
