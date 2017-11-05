from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "http://users.encs.concordia.ca/~c64111/notes/Lectures.htm"
data = {'username': 'COMP6411', 'password': 'S6411C'}
# html = requests.post(url,data)
html = urlopen(url,data)
obj = BeautifulSoup(html)
content = obj.findAll("a")
print(content.read)