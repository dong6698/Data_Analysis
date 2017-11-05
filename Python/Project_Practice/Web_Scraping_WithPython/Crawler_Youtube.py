from urllib.request import urlopen
from bs4 import BeautifulSoup

def getLink(content, page):
    url = 'https://www.youtube.com/results?search_query='+content+'&page=' + str(page)
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find('div', {'id': 'content'}).findAll('h3', {'class': 'yt-lockup-title'})
    return list

page = 1
title = 'python'
while page <= 5:
    bsObj = getLink(title, page)
    for content in bsObj:
        for link in content.findAll('a'):
            print(link.attrs['title'])
            print('https://www.youtube.com' + link.attrs['href'])
    page += 1