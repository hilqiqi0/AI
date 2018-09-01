# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0005_auto_20171117_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='交易时间'),
        ),
    ]
