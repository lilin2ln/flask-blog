# -*- coding: utf-8 -*-
# Author: LDD
# Time: 2018/12/8 14:33
# File: api.py
from . import base
from .model import Model
from ..common import functions


##############################用户####################################
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
    data['salt'] = functions.get_salt(4)
    data['password'] = functions.compile_password(data['password'], data['salt'])
    res = Model('b_users').insert(data)
    return res


def login(user_name, password):
    """用户登录验证
    :param user_name:
    :param password:
    :return:
    """
    user_info = Model('b_users').where({'user_name': user_name}).first()

    if not user_info['detail']:
        return False

    confirm_password = functions.compile_password(password, user_info['detail']['salt'])

    if confirm_password == user_info['detail']['password']:
        return user_info
    else:
        return False


def get_user_info(uid):
    """获取用户信息
    :param uid: 用户id
    :return: {
        "valid": True/False,
        "error_msg": "",
        "detail": {}
    }
    """
    user_info = Model('b_users').where({'uid': uid}).first()

    return user_info


##############################文章####################################
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
    res = Model('b_article').where({'is_recommend': 1}).get()

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
    res = Model('b_article').field('category_id,category_title,count(*) as title_count'). \
        join('b_category', 'b_category.id', 'b_article.category_id').group('category_id').get()

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
    res = Model('b_article').get()

    if not res["valid"]:
        # NOTE: 如果从数据库获取文章列表信息失败，则返回空列表
        return {"detail": []}
    return res


def get_article_list_by_category_id(category_id, offset, limit):
    """通过类型id获取各类文章分页列表
    :param category_id:
    :param offset:
    :param limit:
    :return:
    """
    where = {'category_id': category_id}
    res = Model('b_article').join('b_category', 'b_category.id', 'b_article.category_id').where(where).limit(offset,
                                                                                                             limit).get()
    return res


def get_article_info_by_article_id(article_id):
    """通过文章id获取文章信息
    :param article_id:
    :return:
    """
    where = {'id': article_id}
    res = Model('b_article').where(where).first()
    return res


##############################文章评论####################################
def get_article_comments_by_article_id(article_id):
    """通过文章id获取文章评论列表
    :param article_id:
    :return:
    """
    res = Model('b_article_comments').where({'article_id': article_id}).get()
    return res


def get_article_comment_by_comment_id(comment_id):
    """
    获取单条评论消息
    :param comment_id:
    :return:
    """
    return Model('b_article_comments').where({'id': comment_id}).first()


##############################附件####################################
def get_attachment_list(access_key, item_id):
    """获取附件列表
    :param access_key:
    :param item_id:
    :return:
    """
    where = {'access_key': access_key, 'item_id': item_id}
    return Model('b_attachment').where(where).get()


def get_attachment_info_by_attachment_id(attachment_id):
    """获取单个附件信息
    :param attachment_id:
    :return:
    """
    return Model('b_attachment').where({'id': attachment_id}).first()


##############################友情链接####################################
def get_friendly_link_list():
    """获取友情链接列表
    :return:
    """
    return Model('b_friendly_link').where({'status': 1}).get()


##############################留言####################################
def get_leave_word_list(offset, limit):
    """获取分页留言列表
    :param offset:
    :param limit:
    :return:
    """
    field = 'l.*,u1.user_name as send_user,u2.user_name as receive_user'
    where = {'status': 1}  # status = 1 为正常留言
    return Model('b_leave_word l').field(field).where(where).join('b_users u1', 'u1.id', 'l.uid') \
        .join('b_users u2', 'u2.id', 'l.receive_uid').limit(offset, limit).get()


def get_leave_word_info_by_id(leave_word_id):
    """获取单条留言信息
    :param leave_word_id:
    :return:
    """
    field = 'l.*,u1.user_name as send_user,u2.user_name as receive_user'
    where = {'id': leave_word_id}
    return Model('b_leave_word l').field(field).where(where).join('b_users u1', 'u1.id', 'l.uid') \
        .join('b_users u2', 'u2.id', 'l.receive_uid').first()


def remove_leave_word(leave_word_id):
    """根据留言id删除留言
    :param leave_word_id:
    :return:
    """
    mk = {'id': leave_word_id}
    data = {'status': 0}  # status = 0 表示删除留言
    return Model('b_leave_word').update(mk, data)


