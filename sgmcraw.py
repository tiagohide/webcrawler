import urllib
from random import choice
from sgmllib import SGMLParser

class LinkExplorer(SGMLParser): 
 def reset(self):                              
  SGMLParser.reset(self) 
  self.links = [] # list with the urls

 def start_a(self, attrs):
  """ fill the links with the links in the page """
  for k in attrs:
   if k[0] == 'href' and k[1].startswith('http'): 
    self.links.append(k[1])

def explore(parser,s_url,maxvisit=10,iter=0):
 """ pick a random link in the page s_url
     and follow its links recursively """
 if iter < maxvisit: # it will stop after maxvisit iteration
  print '(',iter,') I am in',s_url
  usock = urllib.urlopen(s_url) # download the page
  parser.reset() # reset the list
  parser.feed(usock.read()) # parse the current page
  if len(parser.links) > 0:
   explore(parser,choice(parser.links),maxvisit,iter+1)
  else: # if the page has no links to follow
   print 'the page has no links'

# test the crawler starting from the python's website
parser = LinkExplorer()
explore(parser,"http://www.modulo.com.br/")
