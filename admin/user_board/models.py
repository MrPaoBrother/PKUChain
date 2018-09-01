# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MonkeyRecord(models.Model):
    class Meta:
        verbose_name = '宠物活动'
        verbose_name_plural = verbose_name
        db_table = 'monkey_record'
    id = models.IntegerField(primary_key=True, auto_created=True)
    address = models.CharField(max_length=255)
    randombackground = models.IntegerField(max_length=5, default=1)
    randomanimals = models.IntegerField(max_length=5, default=0)
    # 猴子穿戴或者没有穿戴的样子
    state = models.IntegerField(max_length=5, default=0)
    go_home_time = models.BigIntegerField(max_length=10, default="")
    description = models.CharField(max_length=300, default="")
    # 默认在家
    is_home = models.IntegerField(default=1)

    def __str__(self):
        return '宠物活动'