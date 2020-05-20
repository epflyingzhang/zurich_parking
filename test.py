# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import os

os.makedirs('download', exist_ok=True)

#while True:
#    time.sleep(6)
#    print("hello world")
#    
from urllib.request import urlopen

while True:
    

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()).replace(':', '_')

    url = 'https://www.pls-zh.ch/plsFeed/rss'
    
    response = urlopen(url)
    data = response.read()
    
    # Write data to file
    filename = "download/{}.xml".format(current_time)
    file_ = open(filename, 'wb')
    file_.write(data)
    file_.close()
    
    time.sleep(5)