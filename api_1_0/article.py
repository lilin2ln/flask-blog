#-*- coding: utf-8 -*-

from flask import jsonify, request, url_for, g
from . import api
from flask_blog.model import api as model_api
import os
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 查询文章标签
@api.route('/article/get_label')
def get_label():
    article_classify_res = model_api.get_article_classify()
    article_classifies = article_classify_res["detail"]
    return jsonify(article_classifies)

@api.route('/article/write', methods=["POST"])
def write_article():
    data = {}
    data["article_title"] = request.form.get("title")
    data["category_id"] = request.form.get("label")
    data["is_top"] = "0"
    data["is_recommend"] = "0"
    data["praises"] = "0"
    data["sort"] = "0"
    data["comments"] = "0"
    data["views"] = "0"
    data["title_fulltext"] = request.form.get("summary")
    data["message"] = "1.jpg"
    data["uid"] = "1"
    data["add_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    article_id = model_api.write_article_base_info(data)

    if article_id == "0" or article_id == 0 or article_id:
        current_path = os.path.abspath(__file__)
        article_lib_path = "/".join(current_path.split("/")[:-2]) + "/templates/article/articles/"
        with open(article_lib_path+str(article_id)+".html", "w") as f:
            f.write(request.form.get("content"))
    else:
        return "fail"
    return "success"