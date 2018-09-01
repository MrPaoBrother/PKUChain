# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

"""
@python_2_unicode_compatible
class BchBlockList(models.Model):
    class Meta:
        verbose_name = "区块列表"
        verbose_name_plural = verbose_name
        db_table = 'bch_block_list'
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name="id")
    hash = models.CharField(max_length=100, default="", verbose_name="hash值")
    txlength = models.CharField(max_length=100, default="", verbose_name="txlength")
    height = models.CharField(max_length=100, default="", verbose_name="区块高度")
    time = models.CharField(max_length=100, default="", verbose_name="区块创建时间")
    size = models.CharField(max_length=100, default="", verbose_name="大小")
    poolInfo = models.CharField(max_length=255, default="", verbose_name="poolInfo")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    extra = models.CharField(max_length=100, default="", verbose_name="其他信息")

    def __str__(self):
        return "bch区块列表"
"""


class PicDetail(models.Model):
    class Meta:
        verbose_name = "宠物相册"
        verbose_name_plural = verbose_name
        db_table = 'pic_detail'
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name="id")
    pic_name = models.CharField(max_length=255, default="", verbose_name="图片名称")
    pic_url = models.CharField(max_length=300, default="", verbose_name="链接")
    pic_type = models.IntegerField(default=0, verbose_name="类型")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")