#-*- coding:utf-8 -*-
from ..base.views import BaseView

class RegisterView(BaseView):

    def __init__(self):
        self.template_name = "auth/register.html"

    def get_data(self):
        return {"hello": "123"}
