# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2023-08-29 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20230829_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comment',
        ),
    ]
