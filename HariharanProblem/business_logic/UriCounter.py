'''
Created on 05-Oct-2016

@author: ishan
'''
from operator import itemgetter
from collections import defaultdict
import os
from functools import partial
import requests

URILIST_PATH = '/home/ishan/sf_shared'
get_abs_file_name = partial(os.path.join, URILIST_PATH) #This helps as we don't need to do os.path.join in loop.

uri_dict = defaultdict(int)

for file_name in os.listdir(URILIST_PATH):#listdir returns only file names not absolute path.
    if file_name.startswith('uri'):
        with open(get_abs_file_name(file_name), 'r') as uris:
            uri_list = uris.readlines()
            for uri in uri_list:
                uri_dict[uri] += 1

most_common_uri = sorted(uri_dict.items(), key = itemgetter(1), reverse = True)[0][0] #Returns a tuple [0][0] specifies uri.

r = requests.get(most_common_uri)
print r.content

