#-*- coding: utf-8 -*-
from flask.views import View
from flask.views import MethodView
from flask import render_template

class BaseView(View):

    def __init__(self):
        self.template_name = None

    def get_template_name(self):
        if not self.template_name:
            raise NotImplementedError
        return self.template_name

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = self.get_data()
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