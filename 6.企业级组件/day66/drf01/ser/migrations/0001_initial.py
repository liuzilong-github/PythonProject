# Generated by Django 4.2.7 on 2023-12-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='提示文本：不能为空', max_length=100, verbose_name='姓名')),
                ('sex', models.BooleanField(default=1, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('class_null', models.CharField(max_length=5, verbose_name='班级编号')),
                ('description', models.TextField(max_length=1000, verbose_name='个性签名')),
            ],
        ),
    ]
