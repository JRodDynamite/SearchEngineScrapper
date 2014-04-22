import time
start_time = time.time()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import google
import yahoo
import bing
from operator import itemgetter

search = "ruby on rails"

g = google.GoogleResults(search,50)
b = bing.BingResults(search,50)
y = yahoo.YahooResults(search,100)

MSE_Result = {}

def MSERank(MSE_Result,eachResult):
    if MSE_Result.get(eachResult[0].encode('utf-8')).get('GRank') == 0 or MSE_Result.get(eachResult[0].encode('utf-8')).get('BRank') == 0:
        return (MSE_Result.get(eachResult[0].encode('utf-8')).get('GRank') + MSE_Result.get(eachResult[0].encode('utf-8')).get('BRank') + eachResult[1].get('YRank'))/float(2)
    else:
        return (MSE_Result.get(eachResult[0].encode('utf-8')).get('GRank') + MSE_Result.get(eachResult[0].encode('utf-8')).get('BRank') + eachResult[1].get('YRank'))/float(3)

for eachResult in sorted(b.items(),key=itemgetter(1)):
    MSE_Result[eachResult[0].encode('utf-8')] = {'MSERank': eachResult[1].get('BRank'),
                                                 'GRank':0,
                                                 'BRank': eachResult[1].get('BRank'),
                                                 'YRank':0
                                                 }
for eachResult in sorted(g.items(),key=itemgetter(1)):
    if eachResult[0] in MSE_Result:
        MSE_Result[eachResult[0].encode('utf-8')] = {'MSERank': (eachResult[1].get('GRank') + MSE_Result.get(eachResult[0].encode('utf-8')).get('BRank'))/float(2),
                                                     'GRank': eachResult[1].get('GRank'),
                                                     'BRank': MSE_Result.get(eachResult[0].encode('utf-8')).get('BRank'),
                                                     'YRank':0
                                                     }
    else:
        MSE_Result[eachResult[0].encode('utf-8')] = {'MSERank': eachResult[1].get('GRank'),
                                                     'GRank': eachResult[1].get('GRank'),
                                                     'BRank':0,
                                                     'YRank':0
                                                     }

for eachResult in sorted(y.items(),key=itemgetter(1)):
    if eachResult[0] in MSE_Result:
        MSE_Result[eachResult[0].encode('utf-8')] = {'MSERank': MSERank(MSE_Result,eachResult),
                                                     'GRank': MSE_Result.get(eachResult[0].encode('utf-8')).get('GRank'),
                                                     'BRank': MSE_Result.get(eachResult[0].encode('utf-8')).get('BRank'),
                                                     'YRank': eachResult[1].get('YRank')
                                                     }
    else:
        MSE_Result[eachResult[0].encode('utf-8')] = {'MSERank':eachResult[1].get('YRank'),
                                                     'GRank': 0,
                                                     'BRank':0,
                                                     'YRank':eachResult[1].get('YRank')
                                                     }

MSE = {}
for each in MSE_Result.items():
    MSE[each[0]] = MSE_Result.get(each[0].encode('utf-8')).get('MSERank')
sorted_MSE = {}
sorted_MSE = sorted(MSE.items(), key=itemgetter(1), reverse=True)
print len(g)
print len(y)
print len(b)
print len(MSE_Result)
print time.time() - start_time, "seconds"
