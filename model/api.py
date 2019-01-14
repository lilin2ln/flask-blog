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
    user_tb = base.Base("b_users") #实例化数据库操作基类
    user_tb.connect() #连接数据库
    res = user_tb.insert(data) #执行插入操作
    user_tb.close() #关闭数据库连接
    return res


def get_article_list():
    """获取文章列表
    :return: {
        "valid": True/False,
        "error_msg": "",
        "detail": [{
            "uid": "文章uid",
            "article_title": "文章标题",
            "message": "文章标题中的图片名称",
            "comments": "文章评论数",
            "views": "文章查看数",
            "add_time": "添加时间",
            "is_top": "文章是否置顶",
            "category_id": "文章类型",
            "praises": "点赞数",
            "is_recommend": "是否推荐"
        }]
    }
    """
    b_article_tb = base.Base("b_article") #实例化数据库操作基类
    b_article_tb.connect() #连接数据库
    res = b_article_tb.show() #执行查询操作
    b_article_tb.close() #关闭数据库连接

    if not res["valid"]:
        #NOTE: 如果从数据库获取文章列表信息失败，则返回空列表
        return []
    return res
