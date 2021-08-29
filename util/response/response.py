#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: response_msg
@time: 2021/5/30 6:20 下午
@desc:
"""
from util.response.code import ResponseCode, ResponseMessage


class ResMsg(object):
    """
    封装响应文本
    """

    def __init__(self, content=None, status_code=ResponseCode.SUCCESS,
                 msg=ResponseMessage.SUCCESS):
        self.content = content
        self.msg = msg
        self.status_code = status_code

    def update(self, content=None, status_code=None, msg=None):
        """
        更新默认响应文本
        :param status_code:响应状态码
        :param content: 响应数据
        :param msg: 响应消息
        :return:
        """
        if status_code is not None:
            self.status_code = status_code
        if content is not None:
            self.content = content
        if msg is not None:
            self.msg = msg

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None and value is not None:
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["status_code"] = body.pop("status_code")
        body["msg"] = body.pop("msg")
        body["content"] = body.pop("content")
        return body
