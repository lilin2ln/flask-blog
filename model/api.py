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
    user_tb = base.Base("b_users")  # 实例化数据库操作基类
    user_tb.connect()  # 连接数据库
    res = user_tb.insert(data)  # 执行插入操作
    user_tb.close()  # 关闭数据库连接
    return res


def get_friendly_links():
    """获取友情链接
    :return: {
        "valid": True/False,
        "error_msg": "",
        "detail": [{
            "link_name": "链接名称",
            "link_url": "链接url"
        }]
    }
    """
    b_friendly_link_tb = base.Base("b_friendly_link")  # 实例化数据库操作基类
    b_friendly_link_tb.connect()  # 连接数据库
    res = b_friendly_link_tb.show()  # 执行查询操作
    b_friendly_link_tb.close()  # 关闭数据库连接

    if not res["valid"]:
        # NOTE: 如果从数据库获取友情链接列表信息失败，则返回空列表
        return {"detail": []}
    return res


def get_user_info(uid):
    """获取用户信息
    :param uid: 用户id
    :return: {
        "valid": True/False,
        "error_msg": "",
        "detail": {}
    }
    """
    user_tb = base.Base("b_users")  # 实例化数据库操作基类
    user_tb.connect()  # 连接数据库
    res = user_tb.show({'uid': uid})
    user_tb.close()  # 关闭数据库连接
    return res


def get_recommend_article_lists():
    """获取推荐文章的简要信息
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
    b_article_tb = base.Base("b_article")  # 实例化数据库操作基类
    b_article_tb.connect()  # 连接数据库
    res = b_article_tb.show({"is_recommend": 1})  # 根据推荐文章键执行查询操作
    b_article_tb.close()  # 关闭数据库连接

    if not res["valid"]:
        # NOTE: 如果从数据库获取文章列表信息失败，则返回空列表
        return {"detail": []}
    return res


def get_article_classify():
    """获取文章分类简要信息
    :return: {
        "valid": True/False,
        "error_msg": "",
        "detail": [{
            "category_id": "标签ID",
            "category_title": "标签名称",
            "title_count": "文章数量"
        }]
    }
    """
    b_category_tb = base.Base("b_category")  # 实例化数据库操作基类
    b_category_tb.connect()  # 连接数据库
    res = b_category_tb.show()  # 执行查询操作
    b_category_tb.close()  # 关闭数据库连接

    category_info = []
    if res["valid"]:
        # NOTE: 如果从数据库获取标签列表信息成功，则给标签赋值
        category_info = res["detail"]

    # NOTE: 查询每个标签所对应的文章数
    for category in category_info:
        b_article_tb = base.Base("b_article")  # 实例化数据库操作基类
        b_article_tb.connect()  # 连接数据库
        article_res = b_article_tb.show({"category_id": category["id"]})  # 根据标签ID执行查询操作
        b_article_tb.close()  # 关闭数据库连接
        if not article_res["valid"]:
            # NOTE: 如果从数据库获取文章信息失败，则给文章数赋值为0
            category["title_count"] = 0
        else:
            # NOTE: 如果从数据库获取文章信息成功，则将文章信息列表的长度赋值给文章数
            category["title_count"] = len(article_res["detail"])
    res["detail"] = category_info
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
    b_article_tb = base.Base("b_article")  # 实例化数据库操作基类
    b_article_tb.connect()  # 连接数据库
    res = b_article_tb.show()  # 执行查询操作
    b_article_tb.close()  # 关闭数据库连接

    if not res["valid"]:
        # NOTE: 如果从数据库获取文章列表信息失败，则返回空列表
        return {"detail": []}
    return res
