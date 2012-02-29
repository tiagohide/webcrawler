"""WEb Crawling
by Tiago Vilas Boas tvilas at gmail dot com
Osiris Web Crawler 1.0

"""
import sys
import re
import time
from sgmllib import SGMLParser

uri = 'http://www.modulo.com.br'

#check_links and check_tags at logical model
class URLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []

	def start_a(self, attrs):
		href = [v for k, v in attrs if k=='href']
		if href:
			self.urls.extend(href)
			

#class Insert(attack): 
	 
#	 def sqlinjection(sql):
#	  print sql
	  
	  #class NoRedirectHandler(urllib2.HTTPRedirectHandler):
#    def http_error_302(self, req, fp, code, msg, headers):
#        infourl = urllib.addinfourl(fp, headers, req.get_full_url())
#        infourl.status = code
#        infourl.code = code
#        return infourl
#    http_error_300 = http_error_302
#    http_error_301 = http_error_302
#    http_error_303 = http_error_302
#    http_error_307 = http_error_302
#opener = urllib2.build_opener(NoRedirectHandler())
#urllib2.install_opener(opener)
#response = urllib2.urlopen('http://google.com')
#if response.code in (300, 301, 302, 303, 307):
#    print 'redirect'




if __name__ == "__main__":
	import urllib
	usock = urllib.urlopen(uri)
	parser = URLLister()
	parser.feed(usock.read())
	parser.close()
	usock.close()
	for url in parser.urls: 
		print url
        # implementar recursive 
	#	urlapp = uri+url
	#	usock = urllib.urlopen(uri)
	#	parser = URLLister()
	#	parser.feed(usock.read())
	#	parser.close()
	#	usock.close()
	#	for url2 in parser.urls: 
	#		print url2
#time.sleep(10)
