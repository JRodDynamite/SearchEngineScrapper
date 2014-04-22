#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import re
from StringIO import StringIO
import gzip

def YahooResults(search,no):
    #mechanize emulates a Browser
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome'),('Accept-encoding','gzip')]

    term = search.replace(" ","+")
    query = "https://search.yahoo.com/search?q=" + term + "&n=" + str(no)

    if br.open(query).info().get('Content-Encoding') == 'gzip':
        buf = StringIO(br.open(query).read())
        f = gzip.GzipFile(fileobj=buf)
        htmltext = f.read()

    soup = BeautifulSoup(htmltext)
    #Since all results are located in the ol tag
    search = soup.findAll('ol')

    searchtext = str(search)

    #Using BeautifulSoup to parse the HTML source
    soup1 = BeautifulSoup(searchtext)
    #Each search result is contained within div tag
    list_items = soup1.findAll('div', attrs={'class':'res'})
    #Each description is contained

    Yahoo_Result = {}

    for li in list_items:
        list_item = str(li)
        title = ""
        soup2 = BeautifulSoup(list_item)
        link = soup2.findAll('a')
        desc = soup2.findAll('div')
        for c in link[0].contents:
            title += c.encode('utf-8')
        d = desc[-1]
        Yahoo_Result[link[0].get('href')] = {
            'title': title.decode('utf-8').replace("<wbr></wbr>","").encode('utf-8'),
            'desc': str(d).split("\">")[1].replace("</div>",""),
            'YRank': no
            }
        no-=1

    return Yahoo_Result
