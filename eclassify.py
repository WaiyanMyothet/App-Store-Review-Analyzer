import sklearn
from sklearn import datasets
from pprint import pprint
import pandas as pd
categories=['Negative','Positive']
cases=sklearn.datasets.load_files("English",description=None,categories=categories,load_content=True,shuffle=True,encoding='utf-8',decode_error='ignore',random_state=0)
#print cases.target_names
#print len(cases.data)
#print("\n".join(cases.data[0].split("\n")[:10]))
#print("\n".join(cases.data[1].split("\n")[:10]))
#print(cases.target_names[cases.target[0]])
#print cases.target[:10]
#for t in cases.target[:10]:
	#print (cases.target_names[t])
from sklearn.feature_extraction.text import  CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmer=WordNetLemmatizer()
stemmer = SnowballStemmer('english')
#cases.data

new_corpus=[' '.join([lemmer.lemmatize(word,'a') for word in word_tokenize(text)])
            for text in cases.data]
new_corpus=[' '.join([lemmer.lemmatize(word,'v') for word in word_tokenize(text)])
            for text in new_corpus]

new_corpus=[' '.join([stemmer.stem(word) for word in word_tokenize(text)])
          for text in new_corpus]
print new_corpus

#print new_corpus
#def wm2df(wm, feat_names
#stopwords=set(stopwords.words('english'))
stop_words = [unicode(x.strip(), 'utf-8') for x in open('stopwords/stopwords.txt','r').read().split('\n')]

count_vect =  CountVectorizer(stop_words=stop_words,ngram_range=(1,2))
X_train_counts = count_vect.fit_transform(new_corpus)
#print count_vect.vocabulary
#print count_vect.vocabulary_.get(u'good')

#tokens=count_vect.get_feature_names()
#print tokens
#pd.DataFrame(data=X_train_counts.toarray(),index=categories,columns=tokens)

#print("\n".join(X_train_counts.data[0].split("\n")[:10]))
#print X_train_counts.shape
#print count_vect.vocabulary_.get(u'algorithm')
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf,cases.target) 
from sklearn.pipeline import Pipeline
text_clf =Pipeline([('vect', CountVectorizer(stop_words=stop_words,ngram_range=(1,2))),
			('tfidf', TfidfTransformer()),
			('clf', MultinomialNB())])
print text_clf.fit(new_corpus, cases.target)
import numpy as np
docs_test=new_corpus
predicted = text_clf.predict(docs_test)
print np.mean(predicted == cases.target)
from sklearn import metrics
print(metrics.classification_report(cases.target, predicted, target_names=cases.target_names))
print metrics.confusion_matrix(cases.target, predicted)
data="awful"
def predict(data):
	docs_new=[]
	textdata=""
	textdata2=""
	textdata1=""
	textdata3=""
	answerdata=[data]
	#print answerdata
	for sdata in word_tokenize(data):
		data=lemmer.lemmatize(sdata,'a') 
		textdata+=data+" "

	for sdata in word_tokenize(textdata):
		data=lemmer.lemmatize(sdata,'v') 
		textdata1+=data+" "
	
	for ldata in word_tokenize(textdata1):
		data2=stemmer.stem(ldata)
		textdata2+=data2+" "
	docs_new=[textdata2]
	print docs_new
	#docs_new = ['just a great and good game','boring and is fake','black screen','never had bad experience','not good','fix the game','haha','fools','awful']
	X_new_counts = count_vect.transform(docs_new)
	#print X_new_counts.toarray()
	#print count_vect.vocabulary_
	#print X_Ne
	#print count_vect.vocabulary
	tokens=count_vect.get_feature_names()
	#print tokens
	#print X_train_counts.shape
	#print X_train_counts.toarray()
	#with open('waiyan.txt','w') as f:
		#f.write(X_train_counts.toarray())
	

	#print X_train_counts.shape
	#print pd.DataFrame(data=X_new_counts.toarray(),index=categories,columns=tokens)
	X_new_tfidf = tfidf_transformer.transform(X_new_counts)
	#print X_new_tfidf.toarray()
	predicted = clf.predict_proba(X_new_tfidf)
	print ("[[ Negative  Positive]]")
	print predicted
	#for i in predicted:
		#pre1=i[0]

	predict = clf.predict(X_new_tfidf)
	for doc, category in zip(docs_new, predict):
		print('%r => %s' % (doc, cases.target_names[category]))
		print '\n'
		return cases.target_names[category],doc,predicted

#predict('awesome')
