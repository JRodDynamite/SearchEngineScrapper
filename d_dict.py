import time
start_time = time.time()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import google
import yahoo
import bing
from operator import itemgetter

search = "ruby on rails"

g = google.GoogleResults(search,10)
b = bing.BingResults(search,11)
y = yahoo.YahooResults(search,10)

MSE_Result = {}

#Scanning Google Search list
for eachResult in g.items():
    MSE_Result[eachResult[0].encode('utf-8')] = {'title': eachResult[1].get('title'),
                                                 'desc': eachResult[1].get('desc'),
                                                 'GRank': eachResult[1].get('GRank'),
                                                 'BRank': 0,
                                                 'YRank': 0,
                                                 'Count': 1,
                                                 'MSERank': eachResult[1].get('GRank')
                                                 }

#Scanning Bing Search list
for eachResult in b.items():
    if eachResult[0] in MSE_Result:
        if eachResult[1].get('BRank') > MSE_Result.get(eachResult[0]).get('GRank'):
            MSE_Result[eachResult[0].encode('utf-8')] = {'title': eachResult[1].get('title'),
                                                         'desc': eachResult[1].get('desc'),
                                                         'GRank': MSE_Result.get(eachResult[0]).get('GRank'),
                                                         'BRank': eachResult[1].get('BRank'),
                                                         'YRank': MSE_Result.get(eachResult[0]).get('YRank'),
                                                         'Count': 2,
                                                         'MSERank': ((MSE_Result.get(eachResult[0]).get('GRank'))+(eachResult[1].get('BRank')))/float(2)
                                                         }
        else:
            MSE_Result[eachResult[0].encode('utf-8')] = {'title': MSE_Result.get(eachResult[0]).get('title'),
                                                         'desc': MSE_Result.get(eachResult[0]).get('desc'),
                                                         'GRank': MSE_Result.get(eachResult[0]).get('GRank'),
                                                         'BRank': eachResult[1].get('BRank'),
                                                         'YRank': MSE_Result.get(eachResult[0]).get('YRank'),
                                                         'Count': 2,
                                                         'MSERank': ((MSE_Result.get(eachResult[0]).get('GRank'))+(eachResult[1].get('BRank')))/float(2)
                                                         }
    else:
        MSE_Result[eachResult[0].encode('utf-8')] = {'title': eachResult[1].get('title'),
                                                     'desc': eachResult[1].get('desc'),
                                                     'GRank': 0,
                                                     'BRank': eachResult[1].get('BRank'),
                                                     'YRank': 0,
                                                     'Count': 1,
                                                     'MSERank': eachResult[1].get('BRank')
                                                     }

#Scanning Yahoo search list
for eachResult in y.items():
    if eachResult[0] in MSE_Result:
        #Comparing with Google
        if eachResult[1].get('YRank') > MSE_Result.get(eachResult[0]).get('GRank'):
            #Comparing with Bing
            if eachResult[1].get('YRank') > MSE_Result.get(eachResult[0]).get('BRank'):
                #This is for Yahoo Rank Being greatest
                MSE_Result[eachResult[0].encode('utf-8')] = {'title': eachResult[1].get('title'),
                                                             'desc': eachResult[1].get('desc'),
                                                             'GRank': MSE_Result.get(eachResult[0]).get('GRank'),
                                                             'YRank': eachResult[1].get('YRank'),
                                                             'BRank': MSE_Result.get(eachResult[0]).get('BRank'),
                                                             'Count': (MSE_Result.get(eachResult[0]).get('Count')+1),
                                                             'MSERank': ((MSE_Result.get(eachResult[0]).get('GRank'))+(MSE_Result.get(eachResult[0]).get('BRank'))+(eachResult[1].get('YRank')))/float((MSE_Result.get(eachResult[0]).get('Count'))+1)
                                                             }
            else:
                #Keeping Title and Description Same
                MSE_Result[eachResult[0].encode('utf-8')] = {'title': MSE_Result.get(eachResult[0]).get('title'),
                                                             'desc': MSE_Result.get(eachResult[0]).get('desc'),
                                                             'GRank': MSE_Result.get(eachResult[0]).get('GRank'),
                                                             'YRank': eachResult[1].get('YRank'),
                                                             'BRank': MSE_Result.get(eachResult[0]).get('BRank'),
                                                             'Count': (MSE_Result.get(eachResult[0]).get('Count'))+1,
                                                             'MSERank': ((MSE_Result.get(eachResult[0]).get('GRank'))+\
                                                              (MSE_Result.get(eachResult[0]).get('BRank'))+\
                                                              (eachResult[1].get('YRank')))/float((MSE_Result.get(eachResult[0]).get('Count'))+1)
                                                             }
        else:
            MSE_Result[eachResult[0].encode('utf-8')] = {'title': MSE_Result.get(eachResult[0]).get('title'),
                                                         'desc': MSE_Result.get(eachResult[0]).get('desc'),
                                                         'GRank': MSE_Result.get(eachResult[0]).get('GRank'),
                                                         'BRank': MSE_Result.get(eachResult[0]).get('BRank'),
                                                         'YRank': eachResult[1].get('YRank'),
                                                         'Count': (MSE_Result.get(eachResult[0]).get('Count'))+1,
                                                         'MSERank': ((MSE_Result.get(eachResult[0]).get('GRank'))+\
                                                              (MSE_Result.get(eachResult[0]).get('BRank'))+\
                                                              (eachResult[1].get('YRank')))/float((MSE_Result.get(eachResult[0]).get('Count'))+1)
                                                         }
    #if URL is new        
    else:
        MSE_Result[eachResult[0].encode('utf-8')] = {'title': eachResult[1].get('title'),
                                                     'desc': eachResult[1].get('desc'),
                                                     'GRank': 0,
                                                     'BRank': 0,
                                                     'YRank': eachResult[1].get('YRank'),
                                                     'Count': 1,
                                                     'MSERank': eachResult[1].get('YRank')
                                                     }


MSE_R = sorted(MSE_Result.items(), key=lambda k:k[1].get('MSERank'), reverse=True)
print len(g)
print len(y)
print len(b)
print len(MSE_Result)
print time.time() - start_time, "seconds"
