# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taobao', '0014_auto_20170728_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='goods',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='goods_id',
            field=models.CharField(default='', max_length=10, verbose_name='商品ID'),
        ),
    ]
