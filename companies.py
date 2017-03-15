#!/usr/bin/python
import sqlite3
database="/Users/awise/Python/Scripts/database.db"
connection=sqlite3.connect(database)
cursor=connection.execute("SELECT * FROM Companies")
print "Content-type: text/html"
print
print "<HTML>"
print " <HEAD>"
print " <TITLE>HTML Tables</TITLE>"
print " </HEAD>"
print " <BODY>"
print " <H1>Musicians</H1>"
print " <TABLE border=1>"
print " <TR>"
print " <TH>Name</TH>"
print " <TH>Age</TH>"
print " <TH>Address</TH>"
print " <TH>Number of Records</TH>"
print " <TH>Band ID</TH>"
print " </TR>"

for row in cursor:
    print "<TR><TD>", row[0], "</TD><TD>", row[1], "</TD><TD>", row[2], "</TD><TD>", row[3], "</TD><TD>", row[4], "</TD></TR>"
    print " </TABLE>"
    print " </BODY>"
    print "</HTML>"
print "Operation done successfully";
connection.close()