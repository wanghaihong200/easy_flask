#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: utils
@time: 2021/6/7 12:05 下午
@desc:
"""
import json, logging
import os, io
import collections
from flask import current_app


def dump_json_file(json_data, json_file_abs_path):
    """ dump json data to file
    """
    file_foder_path = os.path.dirname(json_file_abs_path)
    if not os.path.isdir(file_foder_path):
        os.makedirs(file_foder_path)

    with open(json_file_abs_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def create_scaffold(project_name):
    """ create scaffold with specified project name.
    """
    if os.path.isdir(project_name):
        current_app.logger.warning(u"Folder {} exists, please specify a new folder name.".format(project_name))
        return

    current_app.logger.info("Start to create new project: {}".format(project_name))
    current_app.logger.info("CWD: {}\n".format(os.getcwd()))

    def create_folder(path):
        os.makedirs(path)
        msg = "created folder: {}".format(path)
        current_app.logger.info(msg)

    def create_file(path, file_content=""):
        with open(path, 'w') as f:
            f.write(file_content)
        msg = "created file: {}".format(path)
        current_app.logger.info(msg)

    create_folder(project_name)
    create_folder(os.path.join(project_name, "api"))
    create_folder(os.path.join(project_name, "testcases"))
    create_folder(os.path.join(project_name, "testsuites"))
    create_folder(os.path.join(project_name, "reports"))
    # create_file(os.path.join(project_name, "api", "demo_api.yml"), demo_api_content)
    # create_file(os.path.join(project_name, "testcases", "demo_testcase.yml"), demo_testcase_content)
    # create_file(os.path.join(project_name, "testsuites", "demo_testsuite.yml"), demo_testsuite_content)
    # create_file(os.path.join(project_name, "debugtalk.py"), demo_debugtalk_content)
    # create_file(os.path.join(project_name, ".env"), demo_env_content)
