#from html.parser import HTMLParser
#import urllib.request as urllib2,sys

#class MyHTMLParser(HTMLParser):

#    def handle_data(self, data):
#        print(data)

#parser = MyHTMLParser()
#Opening NYTimes site using urllib2
#html_page = urllib2.urlopen(sys.argv[1])
#page = str(html_page.read())

#Feeding the content
#parser.feed(page)
#parser.close()*/

import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8 
#Accept-Encoding: gzip, deflate 
#Accept-Language: en-US,en;q=0.9 
#Host: infoth.info 
#Upgrade-Insecure-Requests: 1 
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36 
#X-Cache-Req: 1 
#X-Real-Ip: 78.163.114.207

headers = { 
    'User-Agent' : user_agent, 
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9', 
    'Host': 'cse.google.com',
    'Upgrade-Insecure-Requests': '1'
}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)

try: 
    response = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print('HTTP Error code: ', e.code)
    if (e.code == 301):
        print("301")
except urllib.error.URLError as e:
    print('URL Error Reason: ', e.reason)
else: 
    the_page = response.read()   
    print(the_page)

