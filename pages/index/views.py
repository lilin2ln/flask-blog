#-*- coding:utf-8 -*-

from ..base.views import BaseView
from flask_blog.model import api

class IndexView(BaseView):

    def __init__(self):
        self.template_name = 'index/index.html'

    def get_data(self):

        article_lists_res = api.get_article_list() #获取文章列表
        article_lists = article_lists_res["detail"]


        return {"blog_name": "123",
                "blog_description": "456",
                "author": "wi",
                "author_introduce": "testtesttest!",
                "article_lists": article_lists}