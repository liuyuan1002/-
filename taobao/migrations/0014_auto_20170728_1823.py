# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taobao', '0013_auto_20170728_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taobao.goods'),
        ),
    ]
