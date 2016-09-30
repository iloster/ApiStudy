# coding:utf-8
from flask import Blueprint
from flask import request,jsonify
from flask import redirect
from flask import url_for
from flask import render_template
from control.Control_One import Control_One

One_view = Blueprint('One_view',__name__)

#首页 获取最近的十天
#/tab/main/
@One_view.route('/tab/main/')
def getMain():
	control_One = Control_One()
	return control_One.getMain()

#根据月份获取
#/tab/main/getByMonth/<month> 比如 201609
@One_view.route('/tab/main/getByMonth/<month>')
def getMainByMonth(month):
	control_One = Control_One()
	return control_One.getMainByMonth(month)

#阅读
#获取顶部的轮播图片
#/tab/read/carousel/
@One_view.route('/tab/read/carousel/')
def getReadCarousel():
	control_One = Control_One()
	return control_One.getReadCarousel()

#获取文章的列表
#/tab/read/index/
@One_view.route('/tab/read/index/')
def getReadIndex():
	control_One = Control_One()
	return control_One.getReadIndex()

#根据id获取文章详情
#/tab/read/assay/<id>  文章id
@One_view.route('/tab/read/assay/<assayId>')
def getReadAssayById(assayId):
	control_One = Control_One()
	return control_One.getReadAssayById(assayId)

#相关文章推荐
#/tab/read/related/<assayId> 文章id
@One_view.route('/tab/read/related/<assayId>')
def getReadRelatedById(assayId):
	control_One = Control_One()
	return control_One.getReadRelatedById(assayId)

#获取文章的评论 以后所有的分页，分页数都是20
#/tab/read/comment/page/0
@One_view.route('/tab/read/comment/page/<page>')
def getReadCommentByPage(page):
	control_One = Control_One()
	return control_One.getReadCommentByPage()
