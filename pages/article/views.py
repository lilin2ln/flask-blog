# -*- coding:utf-8 -*-

from ..base.views import BaseView
from flask import request
from flask_blog.model import api

from flask_blog.model import api_02


class ArticleView(BaseView):

    def __init__(self):
        self.template_name = 'article/article.html'

    def get_data(self):
        article_id = request.args.get('id')
        article_detail = api_02.get_article_info_by_article_id(article_id)
        return {"article_id": "article/articles/%d.html" % article_detail["detail"]["id"],
                "article": article_detail["detail"]}