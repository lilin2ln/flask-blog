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