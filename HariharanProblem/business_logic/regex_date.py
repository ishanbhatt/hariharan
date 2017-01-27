# -*- coding: utf-8 -*-
'''
Created on Oct 4, 2016

@author: Ishan.Bhatt
'''
def most_common(lst):
    return max(set(lst), key=lst.count)

uri_list = []
with open (r'D:\shared\urilist.txt', 'r') as fp:
    uri_list = fp.readlines()
    
from collections import Counter
count = Counter(uri_list)

print most_common(uri_list)   
# import urllib2
# with urllib2.urlopen(most_common(uri_list)) as response:
#     html = response.read()
#     print html

import operator
from collections import defaultdict
uri_dict = defaultdict(int)

for uri in uri_list:
    uri_dict[uri] += 1

for k,v in uri_dict.iteritems():
    if v > 1:
        print k