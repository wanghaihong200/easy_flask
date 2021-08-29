#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: __init__.py
@time: 2021/5/26 2:04 下午
@desc: 初始化路由，将蓝图注册到app上
"""
from apps.user.urls import easy_users_blue
from blueprints.login import login_blue


def init_route(app):
    app.register_blueprint(easy_users_blue)
    app.register_blueprint(login_blue)

