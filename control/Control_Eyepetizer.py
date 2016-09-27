import urllib2
import json
from flask import jsonify

class Control_Eyepetizer():
	def __init__(self):
		self.m_feedUrl = "http://baobab.wandoujia.com/api/v3/tabs/selected?f=iphone&net=wifi&v=2.5.0"
		self.m_discoverUrl = "http://baobab.wandoujia.com/api/v3/discovery?f=iphone&net=wifi&v=2.5.0"
		self.m_commentUrl = "http://baobab.wandoujia.com/api/v1/replies/video?_s&f=iphone&id=%s&net=wifi&num=20&v=2.5.0"
		self.m_rankList = "http://baobab.wandoujia.com/api/v3/ranklist?&f=iphone&net=wifi&strategy=%s&v=2.5.0" 
		self.m_specialTopic = "http://baobab.wandoujia.com/api/v3/specialTopics?f=iphone&net=wifi&num=20&v=2.5.0"
		self.m_discover1 = "http://baobab.wandoujia.com/api/v3/videos?categoryId=18&f=iphone&net=wifi&num=20&start=0&strategy=date&v=2.5.0"

	def getHtml(self,url):
		request = urllib2.Request(url)
		request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		response = urllib2.urlopen(request)
		return response.read()


	def getFeedSection(self):
		return self.getHtml(self.m_feedUrl)

	def getCommentById(self,videoId):
		url = self.m_commentUrl % videoId
		return self.getHtml(url)
		
	def getDiscover(self):
		return self.getHtml(self.m_discoverUrl)

	def getRankList(self,strategy):
		url = self.m_rankList % strategy
		return self.getHtml(url)

	def getSpecialTopic(self):
		return self.getHtml(self.m_specialTopic)