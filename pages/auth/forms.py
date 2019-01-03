#-*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    account = StringField(label="用户", validators=[DataRequired(), Length(1,32)])
    password = PasswordField(label="密码", validators=[DataRequired()])
    submit = SubmitField(label="登录")

