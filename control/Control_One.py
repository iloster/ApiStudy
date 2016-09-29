# -*- coding: utf-8 -*- 
import urllib2
import json
from flask import jsonify

class Control_One():
	def __init__(self):
		self.m_mainUrl = "http://v3.wufazhuce.com:8000/api/hp/more/0"
		self.m_mainByMonthUrl = "http://v3.wufazhuce.com:8000/api/hp/bymonth/%s"
		self.m_monthList = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		
		self.m_readCarouselUrl = "http://v3.wufazhuce.com:8000/api/reading/carousel?version=v3.5&platform=ios"
		self.m_readIndexUrl = "http://v3.wufazhuce.com:8000/api/reading/index?version=v3.5&platform=ios"
		self.m_readAssayUrl = "http://v3.wufazhuce.com:8000/api/essay/%s?version=v3.5&platform=ios"
		self.m_readRelatedUrl = "http://v3.wufazhuce.com:8000/api/related/essay/%s?version=v3.5&platform=ios"
		self.m_readCommentUrl = "http://v3.wufazhuce.com:8000/api/comment/praiseandtime/serial/181/%s?version=v3.5&platform=ios"

	def getHtml(self,url):
		request = urllib2.Request(url)
		request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		response = urllib2.urlopen(request)
		return response.read()

	def getMain(self):
		return self.getHtml(self.m_mainUrl)

	def getMainByMonth(self,month):
		yearStr = month[0:4]
		monthStr = self.m_monthList[int(month[5:6])]
		timeStr = monthStr+'.'+yearStr
		url = self.m_mainByMonthUrl % timeStr
		return self.getHtml(url)

	def getReadCarousel(self):
		return self.getHtml(self.m_readCarouselUrl)

	def getReadIndex(self):
		return self.getHtml(self.m_readIndexUrl)

	def getReadAssayById(self,assayId):
		url = self.m_readAssayUrl % assayId
		ret = self.getHtml(url)
		retDict = json.loads(ret) 
		return jsonify(retDict)

	def getReadRelatedById(self,assayId):
		url = self.m_readRelatedUrl % assayId
		ret = self.getHtml(url)
		return ret

	def getReadCommentByPage(self,page):
		if int(page) == 0:
			
		else:




