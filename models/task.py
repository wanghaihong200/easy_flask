# -*- coding: utf-8 -*-

from apps.extensions import db
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.dialects.mysql import TINYINT


class Task(db.Model):
    __tablename__ = "task"
    __bind_key__ = 'easy_test_platform'

    task_id = Column(db.BigInteger, primary_key=True, nullable=False)
    type = Column(TINYINT, default=0)
    link_id = Column(db.BigInteger)
    city_id = Column(Integer)
    area_id = Column(Integer)
    block_id = Column(Integer)
    supplier_id = Column(Integer)
    supplier_address = Column(String(255, collation='utf8_unicode_ci'))
    receiver_address = Column(String(255, collation='utf8_unicode_ci'))
    expect_fetch_time = Column(Integer, default=0)
    supplier_lat = Column(db.DECIMAL(precision=10, asdecimal=False), default=0.00)
    supplier_lng = Column(db.DECIMAL(precision=10, asdecimal=False), default=0.00)
    create_time = Column(Integer, default=0)  # 创建时间
    update_time = Column(Integer, default=0)  # 更新时间
    cargo_type = Column(Integer, default=0)  # 商品类型：1.餐饮 2.饮料 3.鲜花 4.票务 5.其他
    delivery_range = Column(Integer, default=0)  # 配送范围：1.立即送-商圈 2.立即送-校园 3.同城
    is_merge = Column(TINYINT, default=0)
    group_type = Column(TINYINT, default=0)
    num = Column(TINYINT, default=0)
    allow_accept_time = Column(Integer, default=0)
    order_destination_lat = Column(db.DECIMAL(precision=10, asdecimal=False), default=0.00)
    order_destination_lng = Column(db.DECIMAL(precision=10, asdecimal=False), default=0.00)
    order_value = Column(db.Float, default=0)
    is_push = Column(TINYINT, default=0)  # 开启推送
    tag = Column(TINYINT, default=0)

    @classmethod
    def search_task_and(cls, **kwargs):
        task = Task.query.filter_by(**kwargs).first()
        return task
