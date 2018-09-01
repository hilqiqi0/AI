# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0004_auto_20171110_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.FloatField(verbose_name='资金', blank=True, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='deal',
            name='time',
            field=models.DateTimeField(verbose_name='交易时间', default=datetime.datetime(2017, 11, 17, 14, 17, 47, 808524)),
        ),
    ]
