#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: user
@time: 2021/5/27 6:10 下午
@desc:
"""
from apps.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"
    __bind_key__ = 'easy_test_platform'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, comment="用户名")
    email = db.Column(db.String(120), index=True, unique=True, comment="邮箱")
    password_hash = db.Column(db.String(128), comment="密码")  # 不保存原始密码
    token = db.Column(db.String(512), comment='web Bearer令牌')
    is_del = db.Column(db.Integer, default='0', comment="是否删除,0：有效， 1：已删除")
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __init__(self, username, password, email):
        self.username = username
        self.password_hash = self.encrypt_password(password)
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def encrypt_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email
        }
