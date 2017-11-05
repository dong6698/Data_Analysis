'''
urllib.error
urllib.request
urllib.parse
BeautifulSoup
'''
'''
from urllib.request import urlopen
from urllib.error import *
from bs4 import BeautifulSoup

# some time open a url can goes wrong like page not found or server not found
try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
else:
    # server is not found, will return a None Object
    if html is None:
        print("URL is not found!!")

bsObj = BeautifulSoup(html.read(), "html.parser")

#  If you attempt to access a tag that does not exist, BeautifulSoup will return a None object
try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print(e)
else:
    if badContent == None:
        print('Tag is not found!!')
    else:
        print(badContent)

print(bsObj.h1)
'''

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
