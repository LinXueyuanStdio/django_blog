# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170501_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='column',
            options={'ordering': ['-name'], 'verbose_name': '栏目', 'verbose_name_plural': '栏目'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=64, verbose_name='标签'),
        ),
    ]
