# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170501_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(db_index=True, max_length=64, verbose_name='标签'),
        ),
    ]