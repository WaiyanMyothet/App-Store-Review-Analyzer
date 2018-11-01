#!/usr/bin/env python
#-*-coding:utf-8 -*-

import sys
import sklearn
import os, sys, codecs
import fileinput
import re

myConsonant = ur"က-အ"
enChar = ur"a-zA-Z0-9"
otherChar = ur"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = ur'္'
ngaThat = ur'င်'
aThat = ur'်'



#Regular expression pattern for Myanmar syllable breaking
#*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
BreakPattern = re.compile(ur"((?<!" + ssSymbol + ur")["+ myConsonant + ur"](?![" + aThat + ssSymbol + ur"])" + ur"|[" + enChar + otherChar + ur"])", re.UNICODE)
#print BreakPattern

def fileopen(inputfile):

	if not sys.stdin.isatty():
		utf8Reader = codecs.getreader('utf8')
	   	inputF = utf8Reader(sys.stdin)
	else:
	   	try:
		      	inputF = codecs.open(inputfile, "rU", encoding='utf-8') #open with universal newline mode (i.e. U)
	   	except:
		       print 'Input file cannot be opened:', inputFile
      #raise SystemExit('Input file cannot be opened!')


	a=[]
	for line in inputF.read().splitlines():
	
		line = BreakPattern.sub(' '+ur"\1", line)
		print line.encode('utf-8')
		#tokenize(line)
		a+=[line]
		
	print a
	inputF = codecs.open(inputfile, "wU", encoding='utf-8') 
	for tokens in a:	
		inputF.write(tokens+'\n' )


def tokenize(string):
	string = BreakPattern.sub(' '+ur"\1", string)
	return string.encode('utf-8')
	
#fileopen("/home/waiyan/Desktop/myanmar/Sport/1")
