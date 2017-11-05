from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_Obj = BeautifulSoup(html, 'html.parser')

#print(soup_Obj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

for img in soup_Obj.findAll('img'):
    print(img)