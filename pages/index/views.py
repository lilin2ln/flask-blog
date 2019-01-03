#-*- coding:utf-8 -*-

from ..base.views import BaseView

class IndexView(BaseView):

    def __init__(self):
        self.template_name = 'index/index.html'

    def get_data(self):
        return {"blog_name": "123",
                "blog_description": "456"}