# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-31 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PicDetail',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('pic_name', models.CharField(default='', max_length=255)),
                ('pic_url', models.CharField(default='', max_length=300)),
                ('pic_type', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'pic_detail',
            },
        ),
    ]