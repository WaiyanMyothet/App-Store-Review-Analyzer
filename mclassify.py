#!/usr/bin/env python
#-*-coding:utf-8 -*-

import sys
import sklearn
import pandas as pd
import os, sys, codecs
import fileinput
import re
from sklearn import datasets
from pprint import pprint
import tokenizer
#reload(sys)
#sys.setdefaultencoding('UTF8')
#tokenizer.fileopen("/home/waiyan/Desktop/MLR/waiyan/Myanmar/myanmar/Sport/2")
#tokenizer.fileopen("/home/waiyan/Desktop/myanmar/Sport/1")
#tokenizer.fileopen("/home/waiyan/Desktop/myanmar/Thar Sis/1")
#data=input("Enter inpu")'


categories=['Politics','Sport','Thar Sis']
cases=sklearn.datasets.load_files("Myanmar/myanmar",description=None,categories=categories,load_content=True,shuffle=True,encoding='utf-8',decode_error='ignore',random_state=0)
#print cases.target_names
#print len(cases.data)
#print("\n".join(cases.data[0].split("\n")[:10]))
#print("\n".join(cases.data[1].split("\n")[:10]))
#print("\n".join(cases.data[2].split("\n")[:10]))
#print(cases.target_names[cases.target[0]])
#print cases.target[:10]
#for t in cases.target[:10]:
	#print (cases.target_names[t])
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

      
	
#stopwords=set(stopwords.words('english'))
count_vect = CountVectorizer(encoding="utf-8",tokenizer=lambda x: x.split())
#print count_vect

X_train_counts = count_vect.fit_transform(cases.data)
tokens=count_vect.get_feature_names()
#print tokens

#print X_train_counts.shape
#print pd.DataFrame(data=X_train_counts.toarray(),index=categories,columns=tokens)
#print count_vect.vocabulary_.get(u'algorithm')
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf,cases.target)
global data
data="  မက်ဆီ"
data=unicode(data,'utf-8')
	
#data.decode("utf-8")
#data=u'\data'

def mpredict(data):

	
	
	data=tokenizer.tokenize(data)
	print (data)
	docs_new=[]
	docs_new+= [data]
#docs_new[0].encode('utf-8')
#[docs_new.encode('utf-8')for docs_new in x]

	X_new_counts = count_vect.transform(docs_new)
	X_new_tfidf = tfidf_transformer.transform(X_new_counts)
	predicted1 = clf.predict_proba(X_new_tfidf)
	#print ("[[ Negative  Positive]]")
	print predicted1
	predicted = clf.predict(X_new_tfidf)
	for doc, category in zip(docs_new, predicted):
		print('%r => %s' % (doc, cases.target_names[category]))
		return cases.target_names[category]
#mpredict(data)
