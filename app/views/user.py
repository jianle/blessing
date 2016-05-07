# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template, Blueprint, redirect, json, request, make_response, url_for, g
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from sqlalchemy import and_

user = Blueprint('user', __name__)

@user.route('/login', methods = ['GET', 'POST'])
def login():
  import hashlib

  print g.user

  if g.user is not None and g.user.is_authenticated():
    return redirect(url_for('/'))

  if request.method == 'GET':
     return render_template("login.html")

  email = request.form["email"]
  password = request.form["password"]

  m = hashlib.md5()
  m.update(password)

  userinfo = User.query.filter(User.email == email).first()
  if userinfo is None:
    msg = '用户不存在, 请先注册'
    return render_template("login.html", email = email, msg = msg)

  userinfo = User.query.filter(and_(User.email == email, User.password == m.hexdigest())).first()
  if userinfo is None:
    msg = '用户名密码不对'
    return render_template("login.html", email = email, password = password)
  else:
    """do nothing"""

  response = make_response(redirect('/'))
  secure_token = create_token(userinfo.id, userinfo.email, request.user_agent)

  response.set_cookie('secure_token', value=secure_token, max_age=2592000)
  login_user(userinfo)
  return response


def create_token(id, email, useragent):
  import hashlib
  import base64
  m = hashlib.md5()
  m.update(str(id) + email + str(useragent))
  return m.hexdigest() + '_' + base64.b64encode(str(id))

def match_user_cookie(secure_cookie, useragent):
  tokens = secure_cookie.split('_')
  import base64
  id = base64.b64decode(tokens[1])
  user = User.query.filter(User.id == int(id)).first()
  if user:
    confirm_secure = create_token(user.id, user.email, useragent)
    if secure_cookie == confirm_secure:
      return user.id
  return None

@user.route('/logout')
@login_required
def logout():
  logout_user()
  response = make_response(redirect('/'))
  response.set_cookie('secure_token', '', 0);
  return response