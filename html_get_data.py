from html.parser import HTMLParser
import urllib.request as urllib2,sys


class MyHTMLParser(HTMLParser):
    tagnames = ['script','style','a']
    datas = ['',' ','\n',' \n','\r','\t','\n\n','\r\n']
    get_data = False
    def handle_starttag(self, tag, attrs):
#        print("Encountered an end tag :", tag)
        if (tag not in self.tagnames):
            self.get_data = True
#            for (key,value) in attrs:
#                print(key,value)
#                if(key == 'href'):
#                    print (value)
        else:
            self.get_data = False
#            print("Encountered a start tag:", tag)
#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if (self.get_data == True ):
            if (len(data.strip())>2):
#            if (data not in self.datas):
                print(sys.argv[1],";", data.rstrip("\\n"))

#    def handle_comment(self, comment):
#        print("Encountered some comment  :", comment)

#    def handle_unknown_decl(self, data):
#        print("Encountered some unknown_decl  :", data)

#    def handle_decl(self, data):
#        print("Encountered some decl  :", data)

parser = MyHTMLParser()
#Opening NYTimes site using urllib2
html_page = urllib2.urlopen(sys.argv[1])
page = str(html_page.read())
#stpage = page.strip()
#print(stpage)

#Feeding the content
parser.feed(page)
parser.close()