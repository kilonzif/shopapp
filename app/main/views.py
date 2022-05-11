from flask import render_template,request,redirect,url_for,abort
from . import main

# Views
@main.route('/')
def index():
    return render_template("index.html")