from html.parser import HTMLParser
import urllib.request as urllib2,sys


class MyHTMLParser(HTMLParser):
    tagname = 'b'
    value = ""
    def handle_starttag(self, tag, attrs):
        if (tag == 'a'):
            self.tagname = 'a' 
            for (key,value) in attrs:
#                print(key,value)
                if(key == 'href'):
                    if(value.find("http") == -1):
                        self.value=sys.argv[1]+value
#                        print (sys.argv[1],value)
                    else:
                        self.value=(value)
#                        print (value)
        else:
            self.tagname = 'b'
#            print("Encountered a start tag:", tag)
#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if (self.tagname == 'a' ):
            self.tagname = 'b'
            print(self.value.strip(), ';', data)
#            print("Link name:", data)

#    def handle_comment(self, comment):
#        print("Encountered some comment  :", comment)

#    def handle_unknown_decl(self, data):
#        print("Encountered some unknown_decl  :", data)

#    def handle_decl(self, data):
#        print("Encountered some decl  :", data)

parser = MyHTMLParser()
#Opening NYTimes site using urllib2
html_page = urllib2.urlopen(sys.argv[1])

#Feeding the content
parser.feed(str(html_page.read()))
parser.close()