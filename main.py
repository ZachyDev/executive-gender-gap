"""
This script will scrape the site littlesis.org for 
the top 500 Forbes Companies

"""
from flask import Flask, render_template
import cgitb
import os
import urllib2
import re

cgitb.enable()

app = Flask(__name__)

# routing/mapping a url on website to a python function 
@app.route('/') #root directory, home page of website, called a decorator
def index():

    # create array to add error pages
    errorPages = [] 
    companyLinks = []
    # companies = []
    # leadershipNames = []
    # personLinks = []
    # url for top 1000 Fortune Companies
    url = "https://littlesis.org/lists/110-fortune-1000-companies-2010/members"
    req = urllib2.Request( url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
    page = urllib2.urlopen(req).read()
    try:
        # create array of companies   
        for i in range(50):
            company = re.findall('"name":"(.*?)"', page, flags=0)[i]
            link = re.findall('"url":"/org/(.*?)/', page, flags=0)[i]
            rank = re.findall('"rank":(.*?),',page, flags=0)[i]
            companyLinks.append([company,rank,link])
        print(companyLinks)
    except urllib2.HTTPError, e:
        print e.fp.read()
  
    return render_template("index.html", companyLinks = companyLinks)

if __name__ == "__main__": #only start web server if this file is called directly  
    port = int(os.environ.get('PORT', 5000)) 
    app.run(debug=True, host='0.0.0.0', port=port) #starts app on web server 

# use companyLinks from above to get current leaders from company page
# try:
#     for i in range(1):
#         url = "https://littlesis.org/entities/" + str(companyLinks[i][2]) + "/relationships#current=true&board=true"
#         req = urllib2.Request( url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
#         page = urllib2.urlopen(req).read()

#         company = re.findall('<title>(.*?) -', page, re.MULTILINE| re.DOTALL|re.IGNORECASE)[0]
#         leadershipNames = re.findall('related_entity_name":"(.*?)"', page, flags=0)
#         personLinks = re.findall('related_entity_url":"/entities/(.*?)/', page,flags=0)
#         for link in personLinks:
#             newlink = link.replace('-', '/',1)
#             link = newlink
#             # print(link)
#         companies.append([company, personLinks])
#     # print(companies)
# except urllib2.HTTPError, e:
#     # print e.fp.read()
#     print('error')