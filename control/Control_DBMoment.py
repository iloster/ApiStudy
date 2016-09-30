# -*- coding: utf-8 -*- 
import urllib2
import json
from flask import jsonify
# import pycurl
from flask import jsonify
import requests

class Control_DBMoment():
	def __init__(self):
		self.m_url = "https://moment.douban.com/api/stream/date/2016-09-29?alt=json&apikey=0bcf52793711959c236df76ba534c0d4&app_version=1.7.4&douban_udid=4263d11d84e2f274f227742d235eab181e005d63&format=full&udid=fcb4f84ed1c194d98341e1c00988adec946e1db2&version=6"
		self.m_url1 = "https://moment.douban.com/api/post/143471?alt=json"
	def getHtml(self,url):		
		# request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		headers = {			
			'Host':'moment.douban.com',
			'Accept':'*/*',
			# 'Cookie':'__ads_session=crqjz+PFygjJZIpqLAA=; bid=c-Url2vhbHM',
			'User-Agent':'api-client/0.1.3 com.douban.daily/1.7.4 iOS/10.0.1 iPhone6,2',
			# "User-Agent":"NewsApp/14.0 iOS/9.3.1 (iPhone6,2)",
			'Accept-Language':'zh-Hans-CN;q=1, en-CN;q=0.9',
			'Accept-Encoding':'gzip, deflate, sdch, br',
			'Connection':'keep-alive',
		}
		response = requests.get(self.m_url,headers = headers,verify=True)
		print response.headers
		print response.request.headers
		return response.content

	def getMoment(self):
		ret = self.getHtml(self.m_url1)
		print ret
		# retstr = json.loads(ret)
		# return jsonify(retstr)
		return ret