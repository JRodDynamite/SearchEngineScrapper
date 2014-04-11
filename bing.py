#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import urllib
from bs4 import BeautifulSoup
import re

def BingResults(search,no):
    #mechanize emulates a Browser
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]

    term = search.replace(" ","+")
    query = "https://www.bing.com/search?q=" + term + "&count=" + str(no)

    htmltext = br.open(query).read()
    ##print htmltext

    soup = BeautifulSoup(htmltext)
    #Since all results are located in the div tag containing the id='results'
    search = soup.findAll('div',attrs={'id':'results'})

    searchtext = str(search[0])

    #Using BeautifulSoup to parse the HTML source
    soup1 = BeautifulSoup(searchtext)
    #Each search result is contained within div tag
    list_items = soup1.findAll('div', attrs={'class':'sa_mc'})

    Bing_Result = {}

    for li in list_items:
        title = ""
        soup2 = BeautifulSoup(str(li))
        link = soup2.findAll('a')
        for c in link[0].contents:
            title += c.encode('utf-8')
        Bing_Result[link[0].get('href')] = {
            'title' : title.decode('utf-8'),
            'desc' : str(soup2.findAll('p')[0]).replace("<p>","").replace("</p>","")
            }

    return Bing_Result
