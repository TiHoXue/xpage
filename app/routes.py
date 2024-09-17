# app/routes.py

from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def homepage():
    return render_template('index.html')
