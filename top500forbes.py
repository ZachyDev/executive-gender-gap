"""
This script will scrape the site littlesis.org for 
the top 500 Forbes Companies

"""

import urllib2
import re


# create array to add error pages
errorPages = [] 
companyLinks = []
companies = []
leadershipNames = []
 
# url for top 1000 Fortune Companies
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
    for i in range(10):
        url = "https://littlesis.org/entities/" + str(companyLinks[i][2]) + "/relationships#current=true&board=true"
        req = urllib2.Request( url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
        page = urllib2.urlopen(req).read()

        company = re.findall('<title>(.*?) -', page, re.MULTILINE| re.DOTALL|re.IGNORECASE)[0]
        leadershipNames = re.findall('related_entity_name":"(.*?)"', page, flags=0)
        companies.append([company, leadershipNames])
    print(companies)
except urllib2.HTTPError, e:
    # print e.fp.read()
    print('error')