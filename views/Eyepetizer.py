# coding:utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request,jsonify
from flask import redirect
from flask import url_for
from flask import render_template
from control.Control_Eyepetizer import Control_Eyepetizer

Eyepetizer_view = Blueprint('Eyepetizer',__name__)


#开眼精选
@Eyepetizer_view.route('/type/feed/')
def getFeedSection():
	control_Eyepetizer = Control_Eyepetizer()
	return control_Eyepetizer.getFeedSection()

#开眼精选里视频评论 根据视频id
@Eyepetizer_view.route('/type/comment/videoId/<videoId>')
def getCommentById(videoId):
	control_Eyepetizer = Control_Eyepetizer()
	return control_Eyepetizer.getCommentById(videoId)

#开眼发现
@Eyepetizer_view.route("/type/discover/")
def getDiscoverSection():
	control_Eyepetizer = Control_Eyepetizer()
	return control_Eyepetizer.getDiscover()