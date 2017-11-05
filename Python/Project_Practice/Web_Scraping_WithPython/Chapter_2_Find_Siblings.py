from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_Obj = BeautifulSoup(html, 'html.parser')

for child in soup_Obj.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(child)