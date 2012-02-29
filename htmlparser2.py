import urllib2 

from HTMLParser import HTMLParser  

class MyHTMLParser(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0 
    self.data = []
  def handle_starttag(self, tag, attrs):
    if tag == 'input':
      for name, value in attrs:
        "if name == 'input':"
        print name,value
        #print "Encountered the beginning of a %s tag" % tag 
        self.recording = 1 


  def handle_endtag(self, tag):
    if tag == 'div':
      self.recording -=1 
      #print "Encountered the end of a %s tag" % tag "

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)
p = MyHTMLParser()
f = urllib2.urlopen('http://www.modulo.com')
html = f.read()
p.feed(html)
"print p.data"
p.close()
