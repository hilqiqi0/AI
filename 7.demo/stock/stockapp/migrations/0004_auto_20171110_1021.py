# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_auto_20171109_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 10, 21, 16, 853012), verbose_name='交易时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, choices=[('0', '男'), ('1', '女')], verbose_name='性别'),
        ),
    ]
