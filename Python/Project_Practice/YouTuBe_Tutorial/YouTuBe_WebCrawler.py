import requests
from bs4 import BeautifulSoup

def trade_spider(char):
    start = char
    while start <= 65:
        st = chr(start)
        url = 'http://www.concordia.ca/academics/graduate.html#' + str(st)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        content = soup.findAll('tbody')
        soup1 = BeautifulSoup(str(content), "html.parser")
        hole = ''
        for link in soup1.findAll('a'):
            url = str(link.get('href')).strip('None')
            if url == '':
                continue
            else:
                hole = 'http://www.concordia.ca/' + url + '\n'
                title = link.string
                print(title)
                print(hole)
        start += 1

trade_spider(65)



