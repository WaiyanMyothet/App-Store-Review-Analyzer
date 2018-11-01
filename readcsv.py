#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
import codecs
import matplotlib.pyplot as plt
import pandas as pd
from eclassify import predict
def readandclassify(csvname):
	readcsv=r'Downloaded_Data/'+csvname+'.csv'
	df=pd.read_csv(readcsv,encoding="utf-8")
	reviews=df.review.tolist()
	codecs.open('Result/'+csvname+'.txt','w',encoding="utf-8")
	pos=0
	neg=0
	for i in reviews:
	
		answer,answer2,answer3=predict(i)
		#for w in answer3:
		#	w1=answer3[0]
		#	w2=answer3[1]
	
		f=codecs.open('Result/'+csvname+'.txt','a',encoding="utf-8")
		#f.write("[[ Negative              Positive ]] \n")
		#f.write("[[ "+w1+"             "+w2+" ]] \n")
 		f.write(answer2+" >>>> "+answer+"\n")
		if answer=="Positive":
		  pos+=1
		else:
		  neg+=1

	print "Positive Numbers: " ,pos
	print "Negative Numbers: " ,neg

	labels = 'Positive', 'Negative'
	sizes = [pos,neg]
	colors = ['gold', 'yellowgreen']
	explode = (0.1, 0)  # explode 1st slice
 
# Plot
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        	autopct='%1.1f%%', shadow=True, startangle=140)
 
	plt.axis('equal')
	plt.show()

#readandclassify("some1")


