# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170501_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=256, verbose_name='标签'),
        ),
    ]
