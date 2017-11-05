import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import re
import urllib.request

url = "http://users.encs.concordia.ca/~c64111/notes/Lectures.htm"
auth = HTTPBasicAuth('COMP6411', 'S6411C')
r = requests.post(url=url, auth=auth)
bsObj = BeautifulSoup(r.text, "html.parser")
content = bsObj.findAll('a', {'href': re.compile(".*.pdf")})
for pdf_link in content:
    #urllib.request.urlretrieve("http://users.encs.concordia.ca/~c64111/notes/"+str(pdf_link.attrs["href"]), "/Users/AlexChen/Desktop/COMP_6411/Slides")

