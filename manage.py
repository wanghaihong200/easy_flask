#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: manage
@time: 2021/5/26 5:33 下午
@desc: 创建一些命令，并且注册到app
"""
from app import app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand


manager = Manager(app)
# 创建命令， python manage.py runserver, 启动app
manager.add_command("runserver", Server(host="127.0.0.1", port=5000, use_debugger=True))

"""
将migrate相关命令注册到manager，python manage.py db init/migrate/updrade 
(python manage.py db init --multidb, 支持多数据库migration, 
 即支持SQLALCHEMY_BINDS定义的额外databases)
"""
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
    manager.debug = True
