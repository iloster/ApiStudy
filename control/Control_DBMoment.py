import urllib2
import json
# import pycurl
from flask import jsonify


class Control_DBMoment():
	def __init__(self):
		self.m_url = "http://moment.douban.com/api/stream/date/2016-08-06?alt=json&app_version=1.7.4&format=full&version=6"
	def getHtml(self,url):
		request = urllib2.Request(url)
		request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		response = urllib2.urlopen(request,context =gcontext)
		return response.read()

	def getMoment(self):
		# buf = cStringIO.StringIO()
		# # return self.getHtml(self.m_url)
		# c = pycurl.Curl()
		# c.setopt(c.URL, 'http://news.ycombinator.com')
		# c.setopt(c.WRITEFUNCTION, buf.write)
		# c.setopt(c.CONNECTTIMEOUT, 5)
		# c.setopt(c.TIMEOUT, 8)
		# c.perform()
		# print buf.getValue()
		# buf.close()
		return "test"