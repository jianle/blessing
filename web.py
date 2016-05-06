# -*- coding:utf-8 -*-
from app import app, db
from flask import redirect, url_for, request, make_response
from flask_login import LoginManager, login_user, current_user

from app.views import *


MODULES = (
  (public, ''),
  (user, '/user')
)


def setting_modules(app, modules):
  """ 注册Blueprint模块 """
  for module, url_prefix in modules:
    app.register_blueprint(module, url_prefix=url_prefix)

setting_modules(app, MODULES)
