#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: project
@time: 2021/6/4 1:59 下午
@desc:
"""
from apps.extensions import db
from datetime import datetime


class Project(db.Model):
    """
    项目信息表
    """
    __tablename__ = "project"
    __bind_key__ = 'easy_test_platform'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, comment="项目名称")
    desc = db.Column(db.String(128), comment="简要介绍")
    owner = db.Column(db.String(64), index=True, comment="负责人")
    is_del = db.Column(db.Integer, default='0', comment="是否删除,0：有效， 1：已删除")
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __init__(self, name, desc, owner):
        self.name = name
        self.desc = desc
        self.owner = owner

    def __repr__(self):
        return '<Project {}>'.format(self.name)

    def to_dict(self):
        return {
            'name': self.name,
            'desc': self.desc,
            'owner': self.owner
        }
