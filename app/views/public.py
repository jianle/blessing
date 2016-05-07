# -*- coding: utf-8 -*-
from app import app
from flask import Blueprint, render_template, request, url_for, make_response
from flask_login import login_user, logout_user, login_required,current_user

public = Blueprint('public', __name__)

@public.route("/")
@login_required
def index():
  return render_template("index.html", text="Hello World")
