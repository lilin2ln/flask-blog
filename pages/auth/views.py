#-*- coding:utf-8 -*-
import random
from ..base.views import BaseView
from ...model.api import register


class RegisterView(BaseView):

    def __init__(self):
        self.template_name = "auth/register.html"

    def get_data(self):
        salt = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 4))
        # print(salt)

        user = {
            'user_name': 'test',
            'true_name': 'test',
            'password': 'pass',
            'salt': salt
        }
        register(user)
        return {"hello": "123"}
