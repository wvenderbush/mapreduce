
import cgi
import cgitb
import random
#cgitb.enable()

d = {}
orig = cgi.FieldStorage()
for k in orig.keys():
    d[k] = orig[k].value
    
x = d["book"]

inSight = open(str(x)+".htm", "r")
book = inSight.read()
inSight.close()
