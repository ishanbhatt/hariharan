'''
Created on Oct 4, 2016

@author: Ishan.Bhatt
'''
import urlparse, os, shutil
from bs4 import BeautifulSoup
import requests
import re
import datetime
import zipfile, tempfile, operator
from collections import defaultdict


URL = r'http://mbd.hu/uris/'

def find_folder(url):
    """
    This method finds the folder name where the zip file is being stored.
    We parse html page and find all <a href /> and then get the folder name using Regex.
    """
    soup = BeautifulSoup(requests.get(url).text, 'lxml') #HTML Parser is lxml
    for a in soup.find_all('a'):
        if re.match(r'\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}',a['href']):
            return a['href']

def find_most_common_set(urilist):
    """
    This method gets the most common uri from the urilist.
    """

    return max(set(urilist), key=urilist.count)

def find_most_common(urilist):
    """
    This method gets the most common uri from the urilist.
    """
    uri_dict = defaultdict(int)
    for uri in urilist:
        uri_dict[uri] += 1
    return sorted(uri_dict.items(), key = operator.itemgetter(1), reverse = True)[0][0]

def get_urllist(url, passwd=None):
    """
    This file returns list of url in the urilist.zip file.
    """
    r = requests.get(url)
    dirpath = tempfile.mkdtemp()
    tempfile_path = os.path.join(dirpath, 'urilist.zip')
    
    with open(tempfile_path, 'wb') as writer:
        writer.write(r.content)
    try:
        with zipfile.ZipFile(tempfile_path) as zf:
            zf.extractall(dirpath, pwd = passwd)
    except:
        raise Exception("THE Zip file is not written to the folder as of now.")
        
    with open(tempfile_path, 'r+') as urifile:
        uris = urifile.readlines()
        common_uri = find_most_common(uris)
        r = requests.get(common_uri.decode('utf-8')) #To resolve unicode decode error as there are some non-ascii characters in uri.
        print r.content #This one should print the content.
    shutil.rmtree(dirpath)

def main(url):

    folder_name = find_folder(url)[:-1]
    old_folder_name = ''
    """
    D:/Foldername contains the name in format 2016_10_04_13_04_41 when we run for the first time. It specifies current timestamp.
    Then we will put this script in crontab entry running every minute to check the folder name.And we will update the file only if folder name has changed.
    """    
    with open(r'D:/Foldername', 'r') as f:
        old_folder_name = f.readline()

    if old_folder_name != folder_name:
        with open(r'D:/Foldername', 'w') as f:
            f.write(folder_name)
        folder_datetime = datetime.datetime.strptime('2016_10_04_13_04_41', "%Y_%m_%d_%H_%M_%S")
        epoch_time = str(int((folder_datetime - datetime.datetime(1970,1,1)).total_seconds()))
        folder_name = folder_name + '/urilist.zip'
        folder_url = urlparse.urljoin(url,folder_name)
        get_urllist(folder_url, epoch_time)

if __name__ == '__main__':
    main(URL)


