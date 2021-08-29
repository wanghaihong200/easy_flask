#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: jwt
@time: 2021/5/31 9:56 下午
@desc:
"""
from flask_jwt_extended import JWTManager
from apps.user.model.user import User
from util.response.code import ResponseCode, headers
from util.response.response import ResMsg

jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@jwt.expired_token_loader
def expired_token_callback(_jwt_header, jwt_data):
    print(_jwt_header)
    print(jwt_data)
    res = ResMsg()
    res.update(msg='token expired', status_code=ResponseCode.FAIL)

    return res.data, headers


@jwt.unauthorized_loader
def unauthorized_callback(jwt_data):
    res = ResMsg()
    res.update(msg='非法访问，请登录！', status_code=ResponseCode.FAIL)
    return res.data, headers
