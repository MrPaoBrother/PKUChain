# -*- coding: utf-8 -*-

from __future__ import absolute_import
from xadmin import views
import xadmin
from .models import *
from users.models import UserProfile
from bch_block_list.models import PicDetail


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    # 设置了一些主页的小工具
    widgets = [
        [
            {"type": "html",
             "title": "Welcome!",
             "content": "<h3>小奶狗管理平台</h3><p>欢迎使用！</p>"},

        ],
        [
            {"type": "qbutton",
             "title": "Quick Start",
             "btns": [{"model": PicDetail},
                      {"model": PicDetail},
                      {"model": UserProfile},
                      {"model": UserProfile},
                      ]},
            {"type": "addform", "model": UserProfile}
        ]
    ]


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    # 可选主题，使用默认主题
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    site_title = '小奶狗数据管理平台'
    site_footer = '小奶狗团队'

    # global_search_models = [BaiduindexSpider, ]
    # 为模型设置图标
    # global_models_icon = {
    #     BaiduindexSpider: "fa fa-eye",
    # }
    # accordion
    menu_style = 'default'


@xadmin.sites.register(MonkeyRecord)
class UserLoginAdmin(object):
    list_display = ('id', 'address', 'randombackground', 'randomanimals', 'state', 'go_home_time', 'description')
    readonly_fields = ('id',)
    search_fields = ['id', 'address']