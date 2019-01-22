#-*- coding: utf-8 -*-
import hashlib
import os
from random import Random


def compile_password(password, salt):
    """编译密码
    :param password:
    :param salt:
    :return:
    """
    password = str_md5(password)
    return str_md5(password + salt)


def str_md5(string):
    """md5加密字符串
    :param string:
    :return:
    """
    md = hashlib.md5()  # 构造一个md5对象
    md.update(string.encode())
    return md.hexdigest()


def get_salt(random_length=4):
    """获取混淆码
    :param random_length:
    :return:
    """
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()

    for i in range(random_length):
        str += chars[random.randint(0, length)]

    return str