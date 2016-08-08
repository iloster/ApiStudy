import urllib2
import json
from flask import jsonify

class Control_ChuiZiReader():
	def __init__(self):
		self.m_homeUrl = "http://reader.smartisan.com/index.php?r=line/show&art_id=10&offset=%d&page_size=20"
		self.m_discoverUrl ="http://reader.smartisan.com/index.php?r=find/getCateList"


	def getHtml(self,url):
		request = urllib2.Request(url)
		request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		response = urllib2.urlopen(request)
		return response.read()

	def getHomePage(self,offset):
		url = self.m_homeUrl % int(offset)
		return self.getHtml(url)

	def getDiscover(self):
		return self.getHtml(self.m_discoverUrl)