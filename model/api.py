# -*- coding: utf-8 -*-
# Author: LDD
# Time: 2018/12/8 14:33
# File: api.py
from . import base

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
    user_tb = base.Base("b_users")
    user_tb.connect()
    res = user_tb.insert(data)
    user_tb.close()
    return res