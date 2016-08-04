# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request,jsonify
from flask import redirect
from flask import url_for
from flask import render_template
import urllib2
import json

# class News(Object):
#     pass

news_view = Blueprint('news', __name__)



@news_view.route('')
def getTopicSet():
	topicSet = urllib2.urlopen("http://c.m.163.com/nc/topicset/ios/subscribe/manage/listspecial.html").read()
	return topicset

@news_view.route('/type/<newsType>/list/<int:page>')
def getListByPage(newsType,page):
	# urlPrefix = "http://c.m.163.com/nc/article/list/";
	f = file("config/news.json");
	s = json.load(f)
	f.close();
	tid = s[newsType]
	url = "http://c.m.163.com/nc/article/list/" + tid + "/" + str(page*10) + "-20.html"
	return url
	# return urllib2.urlopen(url).read()