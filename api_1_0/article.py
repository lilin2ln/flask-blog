#-*- coding: utf-8 -*-

from flask import jsonify, request, url_for, g
from . import api

# 查询文章标签
@api.route('/article/get_label')
def get_label():
    return jsonify({
        '2': 3
    })