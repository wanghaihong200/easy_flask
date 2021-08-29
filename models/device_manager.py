# -*- coding: utf-8 -*-

import datetime

from apps.extensions import db
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DECIMAL
from sqlalchemy.dialects.mysql import TINYINT, BIGINT


class DeviceManager(db.Model):
    __tablename__ = "devicemanager"
    # __table_args__ = {"useexisting": True}

    id = Column(Integer, primary_key=True)
    city = Column(Integer)  # 城市
    device_code = Column(String(40), nullable=True, server_default='', comment="资产编号")  # 资产编号
    device_name = Column(String(20), nullable=True, server_default='')  # 设备名称
    device_type = Column(String(20), nullable=True, server_default='')  # 设备系统类型
    device_version = Column(String(20), nullable=True, server_default='')  # 设备系统版本
    device_serial = Column(String(20), nullable=True, server_default='')  # 设备序列号
    device_admin = Column(String(40), nullable=True, server_default='')  # 设备负责人
    device_user = Column(String(40), nullable=True, server_default='')  # 当前使用者
    use_status = Column(String(10), nullable=True, server_default='')  # 使用状态

    def __init__(self):
        self.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# class AppVersionNotifiter(db.Model):
#
#     __tablename__ = "app_version_notifier"
#     __table_args__ = {"useexisting": True}
#
#     id = Column(Integer, primary_key=True)
#     mail = Column(String(20), nullable=True, server_default='') #通知人邮箱
#     is_del = Column(TINYINT(1), nullable=True, server_default='') #使用状态
#
#     @classmethod
#     def get_mail(cls):
#         mail_info = AppVersionNotifiter.query.filter_by(is_del = 0).all()
#         return mail_info
