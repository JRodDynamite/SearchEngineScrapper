#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import re

#mechanize emulates a Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]

term = "stock market".replace(" ","+")
query = "https://search.yahoo.com/search?q=" + term

htmltext = br.open(query).read()
htm = htmltext

soup = BeautifulSoup(htm)
#Since all results are located in the ol tag
search = soup.findAll('ol')

searchtext = str(search)

#Using BeautifulSoup to parse the HTML source
soup1 = BeautifulSoup(searchtext)
#Each search result is contained within div tag
list_items = soup1.findAll('div', attrs={'class':'res'})
#Each description is contained

for li in list_items:
    list_item = str(li)
    title = ""
    soup2 = BeautifulSoup(list_item)
    link = soup2.findAll('a')
    desc = soup2.findAll('div')
    print link[0].get('href')
    for c in link[0].contents:
        title += c.encode('utf-8')
    print title.decode('utf-8').replace("<wbr></wbr>","")
    d = desc[-1]
    print str(d).split("\">")[1].replace("</div>","").decode('utf-8')
    print ""
