# -*- coding:utf-8 -*-

from ..base.views import BaseView
from flask_blog.model import api


class ArticleView(BaseView):

    def __init__(self):
        self.template_name = 'article/article.html'

    def get_data(self):

        return {"article_name": "article/articles/article001.html"}