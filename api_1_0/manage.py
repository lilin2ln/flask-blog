#-*- coding: utf-8 -*-

from flask import jsonify, request, url_for, g
from . import api
from flask_blog.model import api as model_api
import os
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


@api.route('/manage/recommend', methods=["POST"])
def change_recommend():
    type = request.form.get("action")
    id = request.form.get("id")
    res = model_api.change_recommend({"type": type, "id": id})
    if not res:
        return "fail"
    return "success"


@api.route('/manage/delete_article', methods=["POST"])
def delete_article():
    id = request.form.get("id")
    res = model_api.delete_article({"id": id})
    if not res:
        return "fail"

    current_path = os.path.abspath(__file__)
    article_lib_path = "/".join(current_path.split("/")[:-2]) + "/templates/article/articles/"
    article_path = article_lib_path + str(id) + ".md"
    os.system("rm -rf " + article_path)
    return "success"


@api.route('/manage/edit_user', methods=["POST"])
def edit_user():
    username = request.form.get("username")
    blog_description = request.form.get("blog_description")
    res = model_api.edit_user({"id": 23, "true_name": username, "description": blog_description})
    if not res:
        return "fail"
    return "success"