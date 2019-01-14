#-*- coding:utf-8 -*-

from ..base.views import BaseView
from flask_blog.model import api

class IndexView(BaseView):

    def __init__(self):
        self.template_name = 'index/index.html'

    def get_data(self):
        print api.get_article_list()
        return {"blog_name": "123",
                "blog_description": "456",
                "author": "wi",
                "author_introduce": "testtesttest!"}