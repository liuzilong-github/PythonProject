# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2023-09-05 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
