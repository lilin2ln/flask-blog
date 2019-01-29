#-*- coding:utf-8 -*-
import random
from ..base.views import BaseMethodView
from flask import request,redirect,session


class LoginView(BaseMethodView):

    def __init__(self):
        self.template_name = "auth/login.html"

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '123' and password == '123':
            session["username"] = username
            return redirect("/")
        else:
            return self.render(error=1)