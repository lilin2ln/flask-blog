# -*- coding:utf-8 -*-

from ..base.views import BaseView
from flask_blog.model import api
from flask import request


class ManageView(BaseView):

    def __init__(self):
        self.template_name = 'manage/manage.html'

    def get_data(self):

        # NOTE: 获取文章列表
        article_lists_res = api.get_article_list()
        article_lists = article_lists_res["detail"]
        if request.args.has_key("category_id"):
            # NOTE: 如果用户点击了文章分类，则只列出对应分类的文章
            tmp_lists = []
            for article_list in article_lists:
                if int(article_list["category_id"]) == int(request.args.get("category_id")):
                    tmp_lists.append(article_list)
            article_lists = tmp_lists

        # NOTE: 获取文章分类简要信息
        article_classify_res = api.get_article_classify()
        article_classifies = article_classify_res["detail"]

        # NOTE: 获取推荐文章列表
        article_tuijian_res = api.get_recommend_article_lists()
        article_tuijians = article_tuijian_res["detail"]

        # NOTE: 获取友情链接列表
        friendly_link_res = api.get_friendly_links()
        friendly_links = friendly_link_res["detail"]

        # NOTE: 获取用户信息
        user_info_res = api.get_user_info("23")
        user_info = user_info_res["detail"][0]



        return {"article_lists": article_lists,
                "is_manage": True}