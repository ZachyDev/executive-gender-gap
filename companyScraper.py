"""
This script will scrape the site littlesis.org for top 500 
Forbes companies and the revenue.

"""

import urllib2
import re

# create array to add error pages
errorPages = [] 
companies = []
try:
    for i in range(1,23):
        # get link and update it
        url = "https://littlesis.org/org/" + str(i) + "/a"
        req = urllib2.Request( url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
       
        # create array of companies
    
        page = urllib2.urlopen(req).read()

        company = re.findall('name="title" content="(.*?) -', page, re.MULTILINE| re.DOTALL|re.IGNORECASE)[0]
        companies.append(company)
    print(companies)
except urllib2.HTTPError, e:
    print e.fp.read()
    errorPages.append(i)
    print "error page is"
    print errorPages
    #error on page 24, doesn't exist