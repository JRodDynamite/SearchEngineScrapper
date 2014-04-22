#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
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
    search = soup.findAll('ol',attrs={'id':'b_results'})

    searchtext = str(search[0])

    #Using BeautifulSoup to parse the HTML source
    soup1 = BeautifulSoup(searchtext)
    #Each search result is contained within div tag
    list_items = soup1.findAll('li', attrs={'class':'b_algo'})

    Bing_Result = {}
    no-=1

    for li in list_items:
        title = ""
        soup2 = BeautifulSoup(str(li))
        link = soup2.findAll('a')
        for c in link[0].contents:
            title += c.encode('utf-8')
        Bing_Result[str(link[0].get('href'))] = {
            'title' : str(title),
            'desc' : str(soup2.findAll('p')[0]).replace("<p>","").replace("</p>",""),
            'BRank' : no
            }
        no-=1

    return Bing_Result
