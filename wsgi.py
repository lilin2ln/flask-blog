#-*- coding:utf-8 -*-
import os

from flask import Flask
from . import config


def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config.from_object(config)
    app.debug = app.config['DEBUG']

    register_bp(app)
    register_ext(app)

    from .pages.auth.views import RegisterView
    from .pages.index.views import IndexView

    app.add_url_rule('/auth/register', view_func=RegisterView.as_view(name='register'))
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


def register_bp(app):
    from .api.api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api')


def register_ext(app):
    from .exts import db
    db.init_app(app)
    from .exts import login_manager
    login_manager.init_app(app)
