# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2023-09-17 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20230917_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menus',
        ),
    ]
