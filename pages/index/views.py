# -*- coding:utf-8 -*-

from ..base.views import BaseView
from flask_blog.model import api


class IndexView(BaseView):

    def __init__(self):
        self.template_name = 'index/index.html'

    def get_data(self):

        # NOTE: 获取文章列表
        article_lists_res = api.get_article_list()
        article_lists = article_lists_res["detail"]

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

        print user_info
        return {"blog_name": user_info["true_name"]+u"的博客",
                "blog_description": user_info["description"],
                "author": user_info["true_name"],
                "author_introduce": user_info["description"],
                "article_lists": article_lists,
                "article_classifies": article_classifies,
                "article_tuijians": article_tuijians,
                "friendly_links": friendly_links}