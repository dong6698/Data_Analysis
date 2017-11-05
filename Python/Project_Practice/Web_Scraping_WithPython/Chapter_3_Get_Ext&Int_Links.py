from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	#Finds all links that begin with a "/"
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks

#Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	#Finds all links that start with "http" or "www" that do #not contain the current URL
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace("http://", "").split("/")
	return addressParts

allExternalLinks = set()
allInternalLinks = set()

def getAll_Ext_and_Int_Links(siteURL):
	html = urlopen(siteURL)
	bsObj = BeautifulSoup(html, "html.parser")
	internalLinks = getInternalLinks(bsObj, splitAddress(siteURL)[0])
	externalLinks = getExternalLinks(bsObj, splitAddress(siteURL)[0])
	for link in externalLinks:
		if link not in allExternalLinks:
			allExternalLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allInternalLinks:
			if 'https://' not in link:
				print("About to get link: " + "https://www.douban.com"+link)
			else:
				print("About to get link: " + link)
				allInternalLinks.add(link)
			# getAll_Ext_and_Int_Links(link)

getAll_Ext_and_Int_Links("http://www.douban.com")