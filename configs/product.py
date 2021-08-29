import os
import logging
# from flask_uploads import IMAGES
import time
import pymysql

imgs_path = os.path.dirname(os.path.abspath(__file__))


class Config:
    HOST = ''
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_BINDS = {
                        }
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENCODING = "utf-8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = -1
    DEBUG = True

    CI_USER = ''
    CI_PASSWD = ''
    AUTH_HOST = ''
    SENTRY_DSN = ''
