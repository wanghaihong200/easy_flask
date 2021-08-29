#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: __init__.py
@time: 2021/5/26 1:52 下午
@desc: 初始化app
"""
import logging
from flask import Flask
from configs import config_map
from blueprints import init_route
from apps.extensions import db
from logging.handlers import RotatingFileHandler
from flask_migrate import Migrate
from flask_cors import CORS
from json_web_token.jwt import jwt
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from flask_jwt_extended import create_access_token, set_access_cookies, get_jwt
from flask_jwt_extended import get_jwt_identity
from models import *



# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存日志文件个数上限
file_log_handler = RotatingFileHandler('logs/easy.log', maxBytes=1024*1024*1000, backupCount=10)
# 创建日志记录格式                   日志等级  输出日志信息的文件名   行数       日志信息
formatter = logging.Formatter("%(asctime)s [%(filename)s]: %(lineno)s   [%(levelname)s] : %(message)s")
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__, static_folder='static')

    CORS(app)  # 允许跨域请求

    config_class = config_map.get(config_name)
    print(config_class)
    app.config.from_object(config_class)  # 加载配置

    db.init_app(app)  # 初始化SQLAlchemy
    jwt.init_app(app)
    init_route(app)  # 初始化路由
    return app


# 创建app
app = create_app('develop')

migrate = Migrate().init_app(app, db)  # 初始化migrate


# 每个请求时，如果token即将过期，则刷新
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response
