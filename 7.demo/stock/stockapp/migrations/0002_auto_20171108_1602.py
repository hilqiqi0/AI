# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='time',
            field=models.DateTimeField(verbose_name='交易时间', default=datetime.datetime(2017, 11, 8, 16, 2, 39, 946580)),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='年龄'),
        ),
    ]
