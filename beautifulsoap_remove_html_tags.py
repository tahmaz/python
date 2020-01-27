from bs4 import BeautifulSoup

soup = BeautifulSoup(file, "html.parser")
all_text = ''.join(soup.findAll(text=True))
print(all_text)