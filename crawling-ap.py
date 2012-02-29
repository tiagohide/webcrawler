import httplib
import sys
import re
from HTMLParser import HTMLParser


class miniHTMLParser( HTMLParser ):

  viewedQueue = []
  instQueue = []

  def get_next_link( self ):
    if self.instQueue == []:
      return ''
    else:
      return self.instQueue.pop(0)


  def gethtmlfile( self, site, page ):
    try:
      httpconn = httplib.HTTPConnection(site)
      httpconn.request("GET", page)
      resp = httpconn.getresponse()
      resppage = resp.read()
    except:
      resppage = ""

    return resppage


  def handle_starttag( self, tag, attrs ):
    if tag == 'a':
      newstr = str(attrs[0][1])
      if re.search('http', newstr) == None:
        if re.search('mailto', newstr) == None:
          if re.search('htm', newstr) != None:
            if (newstr in self.viewedQueue) == False:
              print "  adding", newstr
              self.instQueue.append( newstr )
              self.viewedQueue.append( newstr )
          else:
            print "  ignoring", newstr
        else:
          print "  ignoring", newstr
      else:
        print "  ignoring", newstr


def main():

  #if sys.argv[1] == '':
  #  print "usage is ./minispider.py site link"
  #  sys.exit(2)

  mySpider = miniHTMLParser()

  #link = sys.argv[2]
  link = '/'
  while link != '':

    print "\nChecking link ", link

    # Obter o arquivo do site e vincular
    retfile = mySpider.gethtmlfile('www.modulo.com', link )

    # Alimentar o arquivo no analisador HTML
    mySpider.feed(retfile)

    # Procurar pelo retfile aqui

    # Obter o próximo link no pedido de nível transversal
    link = mySpider.get_next_link()

  mySpider.close()

  print "\ndone\n"

if __name__ == "__main__":
  main()
