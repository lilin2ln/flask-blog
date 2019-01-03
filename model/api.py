# -*- coding: utf-8 -*-
# Author: LDD
# Time: 2018/12/8 14:33
# File: api.py
from babyshell.model import base
from babyshell import conf
from babyshell.common import log

CONF = conf.CONF
LOG = log.create_logger(conf.DEFAULT_LOG)


def register(data):
    """register user account
    :param data: {
                    "bs_id": "bs id",
                    "name": "名称",
                    "password": "加密密码",
                    "mobilephone": "加密手机号",
                    "home_id": "home id",
                    "enable_home": 0
                 }
    :return: 成功-True/失败-False
    """
    user_tb = base.Base("user")
    user_tb.connect()
    res = user_tb.insert(data)
    user_tb.close()
    return res