#-*- coding:utf-8 -*-
import random
from ..base.views import BaseMethodView
from flask import request,redirect


class LoginView(BaseMethodView):

    def __init__(self):
        self.template_name = "auth/login.html"

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        print username
        print password
        if username == '123' and password == '123':
            return redirect("/")
        else:
            return self.render(error=1)