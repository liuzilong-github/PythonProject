# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2023-08-13 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('b1', models.DateTimeField(auto_now=True)),
                ('b2', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
