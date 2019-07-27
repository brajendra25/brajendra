# -*- coding: utf-8 -*-
"""
Created on Thu May 10 21:40:20 2018

@author: Anjali Brajendra
"""

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import docx2txt
from docx import Document
from io import StringIO
import nltk
from nltk.corpus import stopwords

#import slate
import numpy as np
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB


'''import docx2txt
my_text = docx2txt.process("E:\Brajendra\\Brajendra_Shukla.doc",'r')
print(my_text)'''
'''
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
word_token=word_tokenize(mytext)
sent_token=sent_tokenize(mytext)
#print(sent_token)
'''
searchKey ="java,jquery,net,.net,net4.5,ASP.net,WCF,API,OOPS"

resultSet = {}
def getText(filename):
    my_text = docx2txt.process(filename)
    #word_token=sent_tokenize(my_text)
    return my_text

text = getText("E:\Brajendra\\demo.docx")
tokens = [t for t in text.split()]
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
     if token in stopwords.words('english'):
         clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)

"""Logic for words frequenct count----"""
searchKeyList = searchKey.split(',')
for key,val in freq.items():
    for value in searchKeyList:
        if value.lower() == str(key).lower():
            resultSet[str(key)] = str(val)
    #print (str(key) + ':' + str(val))

freq.plot(30,cumulative=False)
print(resultSet)













