#-*- coding:utf-8 -*-
import os
from flask import Flask
import sys

def create_app():
    # create and configure the app
    sys.path.append("/root") #将root路径设置为默认目录

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile("config.py", silent=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    from .pages.auth.views import LoginView
    from .pages.index.views import IndexView
    app.add_url_rule('/auth/login', view_func=LoginView.as_view(name='login'))
    app.add_url_rule('/', view_func=IndexView.as_view(name='index'))
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