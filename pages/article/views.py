# -*- coding:utf-8 -*-

from ..base.views import BaseView
from flask import request
from flask_blog.model import api


class ArticleView(BaseView):

    def __init__(self):
        self.template_name = 'article/article.html'

    def get_data(self):
        uid = request.args.get('uid')
        return {"article_name": "article/articles/%s.html" % uid}