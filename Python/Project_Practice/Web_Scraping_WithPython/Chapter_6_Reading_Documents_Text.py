from urllib.request import urlopen
from bs4 import BeautifulSoup

# textpage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# print(textpage.read())

# textpage_2 = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(str(textpage_2.read(), 'utf-8'))

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)