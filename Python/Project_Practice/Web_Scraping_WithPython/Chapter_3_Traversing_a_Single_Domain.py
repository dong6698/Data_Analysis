from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime
'''
before revise the code, the result content have many information we don't want to use
like:
//wikimediafoundation.org/wiki/Privacy_policy
//en.wikipedia.org/wiki/Wikipedia:Contact_us
or:
/wiki/Category:Articles_with_unsourced_statements_from_April_2014
/wiki/Talk:Kevin_Bacon
'''
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# soup_Obj = BeautifulSoup(html, 'html.parser')
# for link in soup_Obj.findAll('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

'''
• They reside within the div with the id set to bodyContent
• The URLs do not contain semicolons
• The URLs begin with /wiki/
'''
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# soup_Obj = BeautifulSoup(html, 'html.parser')
# for link in soup_Obj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

'''
loop the each name link based on different random time int.
'''
random.seed(datetime.datetime.now())
looptime = 5
def getLinks(article_url):
    html = urlopen('http://en.wikipedia.org' + article_url)
    bsObj = BeautifulSoup(html, 'html.parser')
    author_links = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))
    return author_links
links = getLinks('/wiki/Kevin_Bacon')
# while len(links) > 0:
while looptime > 0:
    new_Article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_Article)
    links = getLinks(new_Article)
    looptime -= 1