#-*- coding:utf-8 -*-
import os
from flask import Flask
from datetime import timedelta
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile("config.py", silent=True)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

    from .pages.index.views import IndexView
    from .pages.article.views import ArticleView
    from .pages.write_article.views import WriteArticleView
    from .pages.auth.views import LoginView
    from .pages.manage.views import ManageView
    from .pages.user.views import UserView

    app.add_url_rule('/', view_func=IndexView.as_view(name='index'))
    app.add_url_rule('/login', view_func=LoginView.as_view(name='login'))
    app.add_url_rule('/article', view_func=ArticleView.as_view(name='article'))
    app.add_url_rule('/write_article', view_func=WriteArticleView.as_view(name='write_article'))
    app.add_url_rule('/manage', view_func=ManageView.as_view(name='manage'))
    app.add_url_rule('/user', view_func=UserView.as_view(name='user'))

    from .api_1_0 import api as api_1_0_blueprint    # 注册api蓝图
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1_0')
    return app