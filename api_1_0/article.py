#-*- coding: utf-8 -*-

from flask import jsonify, request, url_for, g
from . import api
from flask_blog.model import api as model_api
import os

# 查询文章标签
@api.route('/article/get_label')
def get_label():
    article_classify_res = model_api.get_article_classify()
    article_classifies = article_classify_res["detail"]
    return jsonify(article_classifies)

@api.route('/article/write', methods=["POST"])
def write_article():
    current_path = os.path.abspath(__file__)
    article_lib_path = "/".join(current_path.split("/")[:-2]) + "/templates/article/articles/"
    with open(article_lib_path+"4.html", "w") as f:
        f.write(str(request.form.get("content")))
    return str(request.form.get("content"))