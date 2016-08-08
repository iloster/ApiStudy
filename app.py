# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template

from views.todos import todos_view
from views.news import news_view
from views.DBMoment import DBMoment_view
from views.ChuiZiReader import ChuiZiReader_view

app = Flask(__name__)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')
app.register_blueprint(news_view, url_prefix='/news')
app.register_blueprint(DBMoment_view, url_prefix='/dbmoment')
app.register_blueprint(ChuiZiReader_view, url_prefix='/chuizireader')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return str(datetime.now())
