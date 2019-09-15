from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
#from moment_apps import views
#from django.view import views
#from django.views.generic.base import TemplateView

def home(request):
	'''
	import urllib
	import re

	link = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/"
	txt = "AGGM.TXT"

	f2 = urllib.urlopen(link + txt)
	z = f2.read()
	lis = [words for words in z.split(" ")]
	#	print(lis)
	d = {}
	for i in lis:
    #print(i)
    	loc = re.search(r"[A-Z]{4}",i)
    	last_date = re.search("[0-9]{4}/[0-9]{2}/[0-9]{2}",i)
    	temp = re.search("^M*[0-9]{2}/M*[0-9]{2}$",i)
    	wind = re.search("[0-9]{5}KT",i)
    	time = re.search("[0-9]{2}:[0-9]{2}",i)
    	if loc:
    		d['station'] =loc.group()
             

    	if wind:
        	d['direction'] = wind.group()[:3]
        	d['velocity'] = wind.group()[3:5]+" knots"
        

    	if last_date:
        	d['date'] = last_date.group()

    	if temp:
        	if temp.group()[0]=="M":
            	d['temperature'] = "-" + temp.group()[1:3]+ " C"
        	else:
        		d['temperature'] = temp.group()[:2]+ " C"
        
    	if time:
        	d['exact_time'] = time.group()+" GMT"

	print(d)
	'''


	return render(request, "home.html", {})
	#return HttpResponse("WORKING BROO")