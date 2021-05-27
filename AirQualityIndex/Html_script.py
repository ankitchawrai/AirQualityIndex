# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:31:25 2021

@author: Ankit Chawrai
"""

import os
import time
import requests
import sys

def retrieve_html():
    print("Started Retrieveing")
    for year in range(2013, 2021):
        for month in range(1,13):
            #print(year,month)
            if (month < 10):
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-42180.html".format(month, year)
            else :
                url = "https://en.tutiempo.net/climate/{}-{}/ws-42180.html".format(month, year)
        
            texts=requests.get(url)
            text_utf = texts.text.encode('utf=8')
        
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year, month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
    print("Finished Retrieveing")    
    

if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print('Time Taken {}'.format(stop_time-start_time))