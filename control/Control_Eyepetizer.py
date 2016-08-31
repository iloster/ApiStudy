import urllib2
import json
from flask import jsonify

class Control_Eyepetizer():
	def __init__(self):
		self.m_feedUrl = "http://baobab.wandoujia.com/api/v3/tabs/selected?f=iphone&net=wifi&v=2.5.0"
		self.m_decoverUrl = "http://baobab.wandoujia.com/api/v3/discovery?f=iphone&net=wifi&v=2.5.0"

	def getHtml(self,url):
		request = urllib2.Request(url)
		request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		response = urllib2.urlopen(request)
		return response.read()


	def getFeedSection(self):
		return self.getHtml(self.m_feedUrl)

	def getDiscover(self):
		return self.getHtml(self.m_decoverUrl)