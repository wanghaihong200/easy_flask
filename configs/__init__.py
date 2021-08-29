#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: __init__.py
@time: 2021/5/26 1:55 下午
@desc:
"""
from configs.ndev import Config as DevConfig
from configs.product import Config as ProductConfig


config_map = {
    'develop': DevConfig,
    'product': ProductConfig,
}
