#-*- coding: utf-8 -*-
from flask.views import View
from flask.views import MethodView
from flask import render_template
from flask_blog.model import api

class BaseView(View):

    def __init__(self):
        self.template_name = None

    def __get_base_info(self):
        # NOTE: 获取用户信息
        user_info_res = api.get_user_info("23")
        self.user_info = user_info_res["detail"][0]

    def get_template_name(self):
        if not self.template_name:
            raise NotImplementedError
        return self.template_name

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = self.get_data()
        self.__get_base_info()
        context["blog_name"] =  self.user_info["true_name"]+u"的博客"
        context["blog_description"] = self.user_info["description"]
        context["true_name"] = self.user_info["true_name"]
        return self.render_template(context)


class BaseMethodView(MethodView):

    def __init__(self):
        self.template_name = None

    def get_template_name(self):
        if not self.template_name:
            raise NotImplementedError
        return self.template_name

    def render(self, error=None):
        return render_template(self.get_template_name(), error=error)

    def get(self, error=None):
        return self.render()

    def post(self):
        return self.render()