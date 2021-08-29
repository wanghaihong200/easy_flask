# -*- coding: utf-8 -*-

import os
from datetime import timedelta

imgs_path = os.path.dirname(os.path.abspath(__file__))


class Config:
    SECRET_KEY = "wanghaihong"
    ENV = 'development'
    DEBUG = True
    HOST = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/zero?charset=utf8'
    SQLALCHEMY_BINDS = {
                        'easy_test_platform': 'mysql+pymysql://root:root@127.0.0.1:3306/easy_test_platform?charset=utf8'
                        }
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENCODING = "utf-8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 动态追踪修改设置
    DEBUG = True

    CI_USER = 'admin'
    CI_PASSWD = 'admin'
    AUTH_HOST = 'http://dauth.{0}.imdada.cn'
    SENTRY_DSN = 'http://762ed02858b142fabe353385fbc9e6c9:83a1806cdb9b44079ce662f41c183db3@sentry.imdada.cn/53'

    # Flask-User settings
    USER_APP_NAME = "Flask-User QuickStart App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form

    # jwt
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-key'
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_CSRF_CHECK_FORM = False
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or timedelta(hours=1)
    PROPAGATE_EXCEPTIONS = True
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_COOKIE_SECURE = False
