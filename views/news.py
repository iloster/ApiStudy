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

# class News(Object):
#     pass

news_view = Blueprint('news', __name__)


@news_view.route('')
def show():
	html = urllib2.urlopen("http://c.m.163.com/nc/topicset/ios/subscribe/manage/listspecial.html").read()
	return html

