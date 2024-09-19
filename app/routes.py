# app/routes.py

from flask import render_template, Blueprint, abort
from markdown2 import markdown
import os

main = Blueprint('main', __name__)

@main.route("/")
def homepage():
    return render_template('index.html')

@main.route("/articles")
def articles():
    # List all markdown files in the articles directory
    article_files = [f for f in os.listdir('app/articles') if f.endswith('.md')]
    articles = [f.replace('.md', '') for f in article_files]
    return render_template('articles.html', articles=articles)

@main.route("/article/<article_name>")
def article(article_name):
    try:
        with open(f'app/articles/{article_name}.md', 'r', encoding='utf-8') as file:
            content = file.read()
            html_content = markdown(content)
        return render_template('article.html', content=html_content, title=article_name)
    except FileNotFoundError:
        abort(404)
