# -*- coding: utf-8 -*-

from __future__ import absolute_import
import xadmin
from .models import *


@xadmin.sites.register(PicDetail)
class BchBlockListAdmin(object):
    list_display = ('id', 'pic_name', 'pic_url', 'pic_type')
    search_fields = ['pic_name', 'pic_url', 'pic_type']
