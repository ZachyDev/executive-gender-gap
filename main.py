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
from getGenders import get_genders

cgitb.enable()

app = Flask(__name__)

# routing/mapping a url on website to a python function 
@app.route('/') #root directory, home page of website, called a decorator
def index():

    leadersDict = get_genders()
    return render_template("index.html", leadersDict = leadersDict)

if __name__ == "__main__": #only start web server if this file is called directly  
    port = int(os.environ.get('PORT', 5000)) 
    app.run(debug=True, host='0.0.0.0', port=port) #starts app on web server 

