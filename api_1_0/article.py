#-*- coding: utf-8 -*-

from flask import jsonify, request, url_for, g
from . import api
from flask_blog.model import api as model_api

# 查询文章标签
@api.route('/article/get_label')
def get_label():
    article_classify_res = model_api.get_article_classify()
    article_classifies = article_classify_res["detail"]
    return jsonify(article_classifies)