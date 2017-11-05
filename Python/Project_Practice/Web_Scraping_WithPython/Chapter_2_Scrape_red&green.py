from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup_Obj = BeautifulSoup(html, "html.parser")
namelist = soup_Obj.findAll('span', {'class':'green'})
for name in namelist:
    # return the specific tag content like :
    # <span class="green">Anna Pavlovna</span>
    print(name)
    # use get_text() method to extract the content text.
    print(name.get_text())
'''
.get_text() strips all tags from the document you are working with and returns a string containing the text only
'''
