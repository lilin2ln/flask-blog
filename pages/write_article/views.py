# -*- coding:utf-8 -*-

from ..base.views import BaseView
from flask import request
from flask_blog.model import api

from flask_blog.model import api_02


class WriteArticleView(BaseView):

    def __init__(self):
        self.template_name = 'write_article/write_article.html'

    def get_data(self):
        return {"is_write": True}