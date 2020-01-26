import requests 
from bs4 import BeautifulSoup
for i in range(10):      # Number of pages plus one 
    url = "https://www.iald.org/Designers?search&page={}".format(i)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
    soup = BeautifulSoup(r.content)
    leads = soup.find_all("h2", {"class":"uk-h3 uk-margin-small"})
    print (leads.string)


