#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: login
@time: 2021/5/27 6:20 下午
@desc:
"""
from flask import Blueprint, jsonify, request, current_app
from apps.extensions import db
from util.response.response import ResMsg
from util.response.code import headers, ResponseCode
from apps.user.model.user import User
from flask_jwt_extended import create_access_token, jwt_required

login_blue = Blueprint("login_blue", __name__)


@login_blue.route('/ping', methods=['GET'])
@jwt_required()
def ping():
    # 用来测试后端api的连通性
    res = ResMsg()
    ping_msg = {
        'app': 'flask'
    }
    res.update(content=ping_msg, msg='连接成功！')

    return jsonify(res.data)


@login_blue.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    res = ResMsg()
    if user and user.check_password(password=password):
        token = create_access_token(identity=user)
        print(token)
        user.token = token
        db.session.commit()

        response = jsonify({
            "status_code": 200,
            "username": user.username,
            "access_token": token,
            "msg": "登录成功！"})
        current_app.logger.info("登录成功")

        return response, headers
    else:
        res.update(msg='用户名或密码错误！', status_code=ResponseCode.FAIL)
        return res.data, headers


@login_blue.route("/logout", methods=['get'])
def logout():
    response = jsonify({"status_code": "200", "msg": "登出成功！"})
    return response
