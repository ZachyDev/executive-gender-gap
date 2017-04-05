"""
Using BeautifulSoup to scrape 

"""

import urllib2
import re
from bs4 import BeautifulSoup
import demjson

# create array to add error pages
errorPages = [] 
companyLinks = []
companies = []
leadershipNames = []
personLinks = []

'''
urls for top 100 companies
'''
url = "https://littlesis.org/lists/110-fortune-1000-companies-2010/members"
req = urllib2.Request( url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
page = urllib2.urlopen(req).read()
try:
    # create array of companies   
    for i in range(10):
        company = re.findall('"name":"(.*?)"', page, flags=0)[i]
        link = re.findall('"url":"/org/(.*?)/', page, flags=0)[i]
        rank = re.findall('"rank":(.*?),',page, flags=0)[i]
        companyLinks.append([company,rank,link])
    # print(companyLinks)
except urllib2.HTTPError, e:
    print e.fp.read()
  
# use companyLinks from above to get current leaders from company page
try:
    for i in range(1):
        url = "https://littlesis.org/entities/" + str(companyLinks[i][2]) + "/relationships#current=true&board=true"
        req = urllib2.Request( url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
        page = urllib2.urlopen(req).read()
        # soup = BeautifulSoup(page, "lxml")
        
         # grab data and convert to list of python dictionaries
        data = re.findall('var data = (.*?)\n', page, flags=0)[0]
        py_obj = demjson.decode(data);

        # grab executives if they are current and put them into list
        for d in py_obj:
            for key in d:
                if d['is_current'] == True and d['is_executive']:
                    leadershipNames.append(d['related_entity_name'])
        leadershipNames = list(set(leadershipNames))
        print(len(leadershipNames))
        print(leadershipNames) 


     
except urllib2.HTTPError, e:
    # print e.fp.read()
    print('error')