# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request,jsonify
from flask import redirect
from flask import url_for
from flask import render_template
from control.Control_ChuiZiReader import Control_ChuiZiReader
ChuiZiReader_view = Blueprint('ChuiZiReader',__name__)

@ChuiZiReader_view.route('/type/home/page/<offset>')
def getHomePage(offset):
	control_ChuiZiReader = Control_ChuiZiReader()
	return control_ChuiZiReader.getHomePage(offset)

@ChuiZiReader_view.route('/type/discover/')
def getDiscover():
	control_ChuiZiReader = Control_ChuiZiReader()
	return control_ChuiZiReader.getDiscover()
