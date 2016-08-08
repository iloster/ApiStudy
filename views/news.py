# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request,jsonify
from flask import redirect
from flask import url_for
from flask import render_template

from control.news import Control_News
# class News(Object):
#     pass

news_view = Blueprint('news', __name__)



@news_view.route('')
def getTopicSet():
	return "hello word"

# 获取某一类型的数据
@news_view.route('/type/<newsType>/list/<int:page>')
def getListByPage(newsType,page):
	control_news = Control_News()
	return control_news.getListByPage(newsType,page)

@news_view.route("/article/postid/<postid>")
def getArticleById(postid):
	control_news = Control_News()
	return control_news.getArticleById(postid)
