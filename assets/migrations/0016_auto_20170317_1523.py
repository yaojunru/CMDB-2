# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-17 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_auto_20170317_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='create_time',
            field=models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]