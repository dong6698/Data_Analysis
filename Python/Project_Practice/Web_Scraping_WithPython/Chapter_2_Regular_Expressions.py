from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_Obj = BeautifulSoup(html, "html.parser")
img_obj = soup_Obj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for img in img_obj:
    print(img.attrs['src'])
