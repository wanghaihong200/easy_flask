#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: views
@time: 2021/5/30 11:13 上午
@desc:
"""
from flask_restful import Resource, fields, marshal_with
from flask import current_app
from apps.user.model.user import User
from util.response.response import ResMsg


class UserResource(Resource):
    user_fields = {
        'id': fields.Integer,
        'username': fields.String,
        'email': fields.String,
        'password_hash': fields.String,
        'create_time': fields.DateTime,
        'update_time': fields.DateTime
    }

    @marshal_with(user_fields)
    def get(self):
        res = ResMsg()
        users = User.query.all()
        print(users[0])
        res.update(content=users[0])
        print(res.data)
        current_app.logger.info("这是user的get请求")
        return users[0]

    def post(self):
        return {'msg': 'post请求'}


if __name__ == '__main__':
    from datetime import datetime
    print(datetime.now())
