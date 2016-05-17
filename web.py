# -*- coding:utf-8 -*-
from app import app, db
from flask import redirect, url_for, request, make_response, g
from flask_login import LoginManager, login_user, current_user
import re

COOKIE_KEY_SECURE_TOKEN = 'secure_token'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = "user.login"

from app.models.user import User
from app.views.user import match_user_cookie

@login_manager.user_loader
def load_user(id):
  return User.query.filter(User.id == id).first()

@app.before_request
def before_request():
  method = request.method.lower()
  path = request.path

  if current_user is None:
    print 'current user is none'
  if not current_user.is_authenticated():
    return

  ignorepath = app.config.get('IGNOREPATH')
  print ignorepath

  pattern = re.compile('%s' % ignorepath)
  if pattern.match(path):
    return

  return

@app.after_request
def after_request(response):
  return response

@login_manager.request_loader
def load_user_from_request(request):
  secure = request.cookies.get(COOKIE_KEY_SECURE_TOKEN)
  if secure:
    id = match_user_cookie(secure, request.user_agent)
    if id:
      userinfo = load_user(id)
      return  userinfo
  return None

@login_manager.unauthorized_handler
def unauthorized():
  secure = request.cookies.get(COOKIE_KEY_SECURE_TOKEN)
  if secure:
    id = match_user_cookie(secure, request.user_agent)
    if id:
      userinfo = load_user(id)
      if userinfo:
        login_user(userinfo)
        url = request.path
        if request.args:
          params = ""
          for k, v in request.args.items():
            params += "%s=%s&" % (k, v)
          url += "?" + params
        return redirect(url or '/')
  return redirect(url_for('user.login'))



from app.views import *


MODULES = (
  (public, ''),
  (user, '/user'),
  (birthday, '/birthday')
)


def setting_modules(app, modules):
  """ 注册Blueprint模块 """
  for module, url_prefix in modules:
    app.register_blueprint(module, url_prefix=url_prefix)

setting_modules(app, MODULES)
