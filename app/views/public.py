# -*- coding: utf-8 -*-
from app import app
from flask import Blueprint, render_template, request, url_for, make_response

public = Blueprint('public', __name__)

@public.route("/")
def index():
  return render_template("index.html", text="Hello World")
