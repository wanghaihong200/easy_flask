#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: auto_test
@time: 2021/6/9 4:56 下午
@desc:
"""
from datetime import datetime

from apps.extensions import db


class AutoTest(db.Model):
    __tablename__ = "auto_test"
    __bind_key__ = 'easy_test_platform'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_name = db.Column(db.String(255), nullable=False)  # 服务名称
    application = db.Column(db.String(255), nullable=False)  # 应用名
    env = db.Column(db.String(50), nullable=False)  # 环境 qa ndev
    commit_id = db.Column(db.String(100), nullable=False)  # git版本号
    # 自动化执行状态，0为待执行，1为执行中，2为执行成功，3为执行失败，4为服务版本失效, 5表示未在auto_api_reord查到数据, 6表示强制停止自动化, 7表示健康检查未通过
    run_status = db.Column(db.SMALLINT, default=0, nullable=False)
    build_no = db.Column(db.String(50), nullable=False)  # qa构建版本号
    auto_build_no = db.Column(db.String(50), default='null', nullable=False)  # jenkins-build-number
    route = db.Column(db.String(50), default='null', nullable=False)  # 链路名
    healthcheck_fail_times = db.Column(db.Integer, default=0, nullable=False)  # 健康检查失败次数
    retest = db.Column(db.SMALLINT, default=0, nullable=False)  # 重测次数
    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")
