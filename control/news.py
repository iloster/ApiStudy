import urllib2
import json
from flask import jsonify
# import jsonify
class Control_News():
	
	def __init__(self):
		self.m_articleUrl = "http://c.m.163.com/nc/article/%s/full.html"

	def getHtml(self,url):
		request = urllib2.Request(url)
		request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
		# request.add_header("User-Agent","NewsApp/14.0 iOS/9.3.1 (iPhone6,2)")
		response = urllib2.urlopen(request)
		return response.read()

	def getListByPage(self,newsType,page):
		f = file("config/news.json");
		s = json.load(f)
		f.close();
		tid = s[newsType]
		url = "http://c.m.163.com/nc/article/list/" + tid + "/" + str(page*10) + "-20.html"
		html = self.getHtml(url)
		ret = json.loads(html)
		print tid
		print ret[tid]
		return json.dumps(ret[tid])

	def getArticleById(self,postid):
		url = self.m_articleUrl % (postid)
		print url
		html =self.getHtml(url)
		ret = json.loads(html)
		return jsonify(ret[postid])


		