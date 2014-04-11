#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import re

def GoogleResults(search,no):
    #mechanize emulates a Browser
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]

    term = search.replace(" ","+")
    query = "https://www.google.co.in/search?q=" + term + "&num=" + str(no)

    htmltext = br.open(query).read()

    soup = BeautifulSoup(htmltext)
    #Since all results are located in the div tag containing the id='search'
    search = soup.findAll('div',attrs={'id':'search'})

    searchtext = str(search[0])

    #Using BeautifulSoup to parse the HTML source
    soup1 = BeautifulSoup(searchtext)
    #Each search result is contained within li tag
    list_items = soup1.findAll('li')
    ##print list_items[0]

    #regex for URL
    uregex = "\/url\?q\=.*?&amp"
    ##regex = "q(?!.*q).*?&amp"
    upattern = re.compile(uregex)

    #regex for title
    tregex = "\">\"?.*?</a>"
    tpattern = re.compile(tregex)

    #regex for description
    ##dregex = "\">\"?.*?</span>"
    ##dpattern = re.compile(dregex)

    Google_Result = {}

    for li in list_items:
        soup2 = BeautifulSoup(str(li))
        links = soup2.findAll('h3')
        title = soup2.findAll('a')
        desc = soup2.findAll('span',attrs={'class':'st'})
        source_url = re.findall(upattern, str(links))
        source_title = re.findall(tpattern,str(title))
        if len(source_url)>0:
            Google_Result[source_url[0].replace("/url?q=","").replace("&amp","")] = {
                'title': source_title[0].replace("\">","").replace("</a>","").decode('utf-8'),
                'desc': str(desc[0]).replace("<span class=\"st\">","").replace("</span>","").decode('utf-8')
                }
##            source_url[0] = source_url[0].replace("/url?q=","").replace("&amp","")
##            source_title[0] = source_title[0].replace("\">","").replace("</a>","")
##            desc[0] = str(desc[0]).replace("<span class=\"st\">","").replace("</span>","")
##            print str(source_url[0]).decode('utf-8')
##            print str(source_title[0]).decode('utf-8')
##            print str(desc[0]).decode('utf-8')

    return Google_Result
