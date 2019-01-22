#-*- coding:utf-8 -*-
import os
from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile("config.py", silent=True)

    from .pages.index.views import IndexView
    from .pages.article.views import ArticleView
    app.add_url_rule('/', view_func=IndexView.as_view(name='index'))
    app.add_url_rule('/article', view_func=ArticleView.as_view(name='article'))
    return app

"""
页面权限控制
0: 管理员
1: 用户
2: 所有用户
"""
permission = {
    "auth": "2",
    "index": "2"
}