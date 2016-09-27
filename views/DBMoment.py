# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request,jsonify
from flask import redirect
from flask import url_for
from flask import render_template
from control.Control_DBMoment import Control_DBMoment
DBMoment_view = Blueprint("DBMoment_view",__name__)

@DBMoment_view.route('/')
def getMoment():
	control_DBMoment = Control_DBMoment()
	return control_DBMoment.getMoment()