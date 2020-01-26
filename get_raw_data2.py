from bs4 import BeautifulSoup
import requests, sys
page_link = sys.argv[1]
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
#---other options----------
#requests.post('https://httpbin.org/post', data={'key':'value'})
#requests.put('https://httpbin.org/put', data={'key':'value'})
#requests.delete('https://httpbin.org/delete')
#requests.head('https://httpbin.org/get')
#requests.patch('https://httpbin.org/patch', data={'key':'value'})
#requests.options('https://httpbin.org/get')

# Collect and parse first page
response = requests.get(page_link)
#response = requests.get(
 #   page_link,
    #params={
    #    'oe' : 'utf8',
    #    'ie' : 'utf8',
    #    'source' : 'uds',
    #    'q' : '"Hay House U" "marketing"',
    #    'safe' : 'off',
    #    'cx' : '011658049436509675749:gkuaxghjf5u',
    #    'start' : '0'
    #},
 #   headers={
 #       'Metod' : 'GET',
        #'Path' : '/cse?oe=utf8&ie=utf8&source=uds&q=%22Hay%20House%20U%22%20%22marketing%22&safe=off&sort=&cx=011658049436509675749:gkuaxghjf5u&start=0',
 #       'User-Agent' : user_agent,
 #       'Accept-Encoding': 'gzip, deflate',
 #       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 #       'Accept-Language': 'en-US,en;q=0.9', 
        #'Host': 'cse.google.com',
 #       'Upgrade-Insecure-Requests': '1'
        #'scheme' : 'https',
        #'cookie' : 'NID=160=P4sGo-G4TQQQ3EkcNhPfCSSAIJVURDrBMYnVTDeBUSLcbeLW1elYz3C0NzotcwJkGtJapuP64qEz_NpKVnJXt7BBjczEosOkKTkT5WH5BUy1AQY-idutxeh4zU_aN5emcF3fCBZpemWS2fES9HeNzF4SsJ3OYEzg2_ZDR3nXphupux1RQZO9JMcG8Q; 1P_JAR=2019-02-22-19',
        #'x-clinet-data' : 'CJa2yQEIpLbJAQjEtskBCKmdygEIqKPKAQixp8oBCL+nygEI4qjKARj5pcoB'
  #  },
#)
#response.encoding = 'utf-8'
#print(response.json())
#print(response.status_code)
#print(response.headers)
print(response.text)


#soup = BeautifulSoup(response.text, 'html.parser')

#print(response.text)