import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://www.google.com"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()

soup = BeautifulSoup(document) 

# retorna uma lista com todos os links do documento
links = soup.findAll('a')  

for link in links:
     print link
