#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: urls
@time: 2021/5/30 11:13 上午
@desc:
"""
from flask import Blueprint, jsonify, request
from apps.user.model.user import User
from apps.extensions import db
from util.response.response import ResMsg
from util.response.code import ResponseCode, headers
from flask_jwt_extended import jwt_required,get_jwt_identity


easy_users_blue = Blueprint("easy_users_blue", __name__, url_prefix='/user')


@easy_users_blue.route('/register', methods=['POST'])
def user_register():
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)
    email = data.get('email', None)

    res = ResMsg()

    if username and password and email:
        user = User(username, password, email)
        db.session.add(user)
        db.session.commit()
        content = {
            'username': username,
            "user_id": user.id
        }
        res.update(content=content, msg='注册成功！')
    else:
        res.update(status_code=ResponseCode.FAIL, msg='注册失败，用户名、密码、邮箱不能为空！')

    return res.data, headers


@easy_users_blue.route('/get_user', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    print(current_user)
    username = request.args.get('username')
    user_info = User.query.filter_by(username=username).first().to_dict()
    res = ResMsg()
    res.update(content=user_info)
    response = res.data

    return response, headers

