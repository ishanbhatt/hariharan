'''
Created on Oct 4, 2016

@author: Ishan.Bhatt
'''
import ftplib
f = ftplib.FTP()
f.connect("ftp://mbd.hu/uris/")
f.login()
ls = []
f.retrlines('MLSD', ls.append)
for entry in ls:
    print entry