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

        return {"blog_name": "123",
                "blog_description": "456",
                "author": "wi",
                "author_introduce": "testtesttest!",
                "article_lists": article_lists,
                "article_classifies": article_classifies,
                "article_tuijians": article_tuijians,
                "friendly_links": friendly_links}