# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0002_auto_20171108_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 17, 19, 31, 667397), verbose_name='交易时间'),
        ),
    ]
