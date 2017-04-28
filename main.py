"""
This script will scrape the site littlesis.org for 
the top 500 Forbes Companies and the gender of their executives 

"""
from flask import Flask, render_template
import cgitb
import os
import urllib2
import re
import demjson
import csv
# from getGenders import get_genders
import sqlite3 as sql

cgitb.enable()

app = Flask(__name__)

# routing/mapping a url on website to a python function 
@app.route('/') #root directory, home page of website, called a decorator
def index():
  con = sql.connect("database.db")
  con.row_factory = sql.Row
   
  cur = con.cursor()

  cur.execute("SELECT DISTINCT * from leaders")
  rows = cur.fetchall();
  print(type(rows))

  return render_template("index.html", rows = rows)

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()

   cur.execute("SELECT DISTINCT * FROM leaders")
   
   rows = cur.fetchall();
   return render_template("list.html", rows = rows)

if __name__ == "__main__": #only start web server if this file is called directly  
    port = int(os.environ.get('PORT', 5000)) 
    app.run(debug=True, host='0.0.0.0', port=port) #starts app on web server 

