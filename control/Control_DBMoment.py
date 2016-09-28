# -*- coding: utf-8 -*- 
import urllib2
import json
from flask import jsonify
# import pycurl
from flask import jsonify
import ssl
import gzip,StringIO
import platform


class Control_DBMoment():
	def __init__(self):
		self.m_url = "https://moment.douban.com/api/stream/date/2016-08-06?alt=json&app_version=1.7.4&format=full&version=6"
	
	def getHtml(self,url):		
		# request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		header = {			
			'Host':'moment.douban.com',
			'Accept':'*/*',
			# 'Cookie':'__ads_session=crqjz+PFygjJZIpqLAA=; bid=c-Url2vhbHM',
			'User-Agent':'api-client/0.1.3 com.douban.daily/1.7.4 iOS/10.0.1 iPhone6,2',
			'Accept-Language':'zh-Hans-CN;q=1, en-CN;q=0.9',
			'Accept-Encoding':'gzip, deflate',
			'Connection':'keep-alive',
		}
		gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
		request = urllib2.Request(url,None,header)
		response = urllib2.urlopen(request,context=gcontext)
		compressedData = response.read()
		compressedStream=StringIO.StringIO(compressedData)
		gzipper=gzip.GzipFile(fileobj=compressedStream)
		data=gzipper.read()
		return data

	def getMoment(self):
		ret = self.getHtml(self.m_url)
		retstr = json.loads(ret)
		return jsonify(retstr)