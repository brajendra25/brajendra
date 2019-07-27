# -*- coding: utf-8 -*-
"""
Created on Thu May 10 21:00:05 2018

@author: Anjali Brajendra
"""
"""---- This Program is for reading the web page and count
words frequency without stopwords and plot a graph """
from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords
nltk.download()
print("done")
response = urllib.request.urlopen('http://www.webmindservices.com/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
     if token in stopwords.words('english'):
         clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)

"""Logic for words frequenct count----""
for key,val in freq.items():
    print (str(key) + ':' + str(val))
    """
freq.plot(20,cumulative=False)