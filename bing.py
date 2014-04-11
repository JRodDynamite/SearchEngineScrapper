#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import urllib
from bs4 import BeautifulSoup
import re

#mechanize emulates a Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]

term = "stock market".replace(" ","+")
query = "https://www.bing.com/search?q=" + term

htmltext = br.open(query).read()
#print htmltext

soup = BeautifulSoup(htmltext)
#Since all results are located in the div tag containing the id='results'
search = soup.findAll('div',attrs={'id':'results'})

searchtext = str(search[0])

#Using BeautifulSoup to parse the HTML source
soup1 = BeautifulSoup(searchtext)
#Each search result is contained within div tag
list_items = soup1.findAll('div', attrs={'class':'sa_mc'})

#Each description is contained
##list_items_desc = soup1.findAll('p')

#List of first search result
#print list_items[0]

##regex = "q(?!.*q).*?&amp"
##pattern = re.compile(regex)

for li in list_items:
    title = ""
    soup2 = BeautifulSoup(str(li))
    link = soup2.findAll('a')
    print link[0].get('href')
    for c in link[0].contents:
        title += c.encode('utf-8')
    print title.decode('utf-8')
    print str(soup2.findAll('p')[0]).replace("<p>","").replace("</p>","")
    print ""
