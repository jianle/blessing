# -*- coding: utf-8 -*-
from app import app
from flask import Blueprint, render_template, request, url_for, make_response
from flask_login import login_user, logout_user, login_required,current_user

birthday = Blueprint('birthday', __name__)

@birthday.route('/')
@login_required
def list():
  return render_template("birthday/list.html", text="Hello guys")