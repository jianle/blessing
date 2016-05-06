from app import app, db
from flask import render_template, Blueprint, redirect, json, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User

user = Blueprint('user', __name__)

@user.route('/login')
def login():
  rs = User.query.filter(User.id == 1).first()
  return render_template("login.html", rs=rs)
