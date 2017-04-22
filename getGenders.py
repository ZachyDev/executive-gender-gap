"""
Using BeautifulSoup to scrape 

"""

import urllib2
import re
from bs4 import BeautifulSoup
import demjson
import gender_guesser.detector as genderg
import sqlite3 as sql

# conn = sql.connect('database.db')
# print "Opened database successfully"

# cur = conn.cursor()

# cur.execute("""CREATE TABLE leaders(name text, link text, gender text)""")
# cur.execute('DROP TABLE leaders')
# print "Table deleted"
# conn.close()

def get_genders():
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
    except urllib2.HTTPError, e:
        print e.fp.read()
      
    '''
    use companyLinks from above to get current leaders and gender from each company page
    '''
    try:
        for i in range(1):
            url = "https://littlesis.org/entities/" + str(companyLinks[i][2]) + "/relationships#current=true&board=true"
            req = urllib2.Request( url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
            page = urllib2.urlopen(req).read()
           
             # grab data and convert to list of python dictionaries
            data = re.findall('var data = (.*?)\n', page, flags=0)[0]
            py_obj = demjson.decode(data);
            
            '''
            # grab executives, links, and gender if they are current and put them into list
            '''
            for d in py_obj:
                if d['is_current'] == True and d['is_executive']:
                    # leadershipNames.append(d['related_entity_name'])
                    personLinks.append(d['related_entity_url'][9:].replace('-', '/',1)) #grab link and edit for scraping
                    name = d['related_entity_name']
                    link = d['related_entity_url'][9:].replace('-', '/',1)
                    url2 = "https://littlesis.org/person" + link
                    req2 = urllib2.Request(url2, None, headers = {'User-Agent': 'Mozilla/5.0'})
                    page2 = urllib2.urlopen(req2).read() 
                    try:
                        gender = re.findall('(Female|Male)',page, flags=0 )[0]
                    except (urllib2.HTTPError, IndexError):
                        gDetector = genderg.Detector()
                        gender = gDetector.get_gender(name.split(' ')[0])
                    try:
                        with sql.connect('database.db') as con:
                            cur = con.cursor()
                            cur.execute("""INSERT INTO leaders (name,link,gender) VALUES (?,?,?)""",(name, link,gender))
                            con.commit()
                    except:
                        con.rollback()
                        print "error in insert operation"
                    finally:
                        con.close()        
    except urllib2.HTTPError, e:
        # print e.fp.read()
        print('error')

if __name__ == "__main__":
    leadersDict2 = get_genders()
    