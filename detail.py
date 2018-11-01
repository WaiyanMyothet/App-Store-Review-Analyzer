#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Aug 08, 2018 11:59:29 AM
import nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
lemmer=WordNetLemmatizer()
stemmer = SnowballStemmer('english')

def readcsvandtoken(csv):
	global token
	token=[]

	readcsv=r'Downloaded_Data/'+csv+'.csv'
	df=pd.read_csv(readcsv,encoding="utf-8")
	reviews=df.review.tolist()
	for i in reviews:
	
		tokens=word_tokenize(i)
		token+=[tokens]
	return token	

def tokenize(csv):
	a=readcsvandtoken(csv)
	print a

def removestopwords(csv):
	a=readcsvandtoken(csv)
	stop=[]
	sen=''
	docs_new=[]
	textdata=""
	textdata2=""
	for w in a:
		for i in w:
			if i.lower() not in stopwords.words('english') and i not in string.punctuation:
				print i.lower(),
			  
			  
                print '\n'

def stemm(csv):
	a=readcsvandtoken(csv)
	for w in a:
		for i in w:
			if i.lower() not in stopwords.words('english') and i not in string.punctuation:
				#print i.lower(),
				data=lemmer.lemmatize(i,'a')
				data=stemmer.stem(data)
				print data,

		print '\n'
#removestopwords('941069339')