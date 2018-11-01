#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import time
import csv
import tkMessageBox

def getJson(url):
    response = urlopen(url)
    data = str(response.read())
    return json.loads(data)



def getReviews(appID):
    csvname=r'Downloaded_Data/'+str(appID)+'.csv'
    with open(csvname, 'wb') as f:
	writer =csv.writer(f)
	Titles = ['review_id', 'title', 'author', 'author_url', 'version', 'rating', 'review', 'vote_count']
	writer.writerows([Titles])
    	page=1
    	while page<=10:
	   try:
	      url = 'https://itunes.apple.com/rss/customerreviews/id=%s/page=%d/sortby=mostrecent/json' % (appID, page)
	      print url
	      data = getJson(url).get('feed')
	      if data.get('entry') == None:
		getReviews(appID, page+1)
		return
	

	      for entry in data.get('entry'):
	        if entry.get('im:name'): continue
		
		review_id = entry.get('id').get('label')
		title = entry.get('title').get('label')
		author = entry.get('author').get('name').get('label')
		author_url = entry.get('author').get('uri').get('label')
		version = entry.get('im:version').get('label')
		rating = entry.get('im:rating').get('label')
		review = entry.get('content').get('label')	
		vote_count = entry.get('im:voteCount').get('label')

		csvData = [review_id, title.replace('"', '""'), author, author_url, version, rating, review.replace('"', '""'),
 vote_count]
		csvData=[s.encode('utf-8') for s in csvData]
		

		#print '"'+'","'.join(csvData)+'"'
		writer.writerows([csvData])

	      
	   except Exception as e:
	      break
	   page+=1
	   
	with open(csvname, 'rb') as f:
	      	row_count = sum(1 for row  in f)
		print "Done"
	        
		tkMessageBox.showinfo('Result',str(row_count)+" reviews were saved \n from App Store")
		return row_count	

#getReviews(1144018570)

    	

