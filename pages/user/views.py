# -*- coding:utf-8 -*-

from ..base.views import BaseView
from flask_blog.model import api
from flask import request


class UserView(BaseView):

    def __init__(self):
        self.template_name = 'user/user.html'

    def get_data(self):

        # NOTE: 获取友情链接列表
        friendly_link_res = api.get_friendly_links()
        friendly_links = friendly_link_res["detail"]

        return {"friendly_links": friendly_links, "is_user": True}