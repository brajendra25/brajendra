# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:51:16 2018

@author: Anjali Brajendra
"""

"""from io import BytesIO
from PIL import Image, ImageDraw

image = Image.new("RGB", (300, 50))
draw = ImageDraw.Draw(image)
draw.text((0, 0), "This text is drawn on image")

byte_io = BytesIO()

image.save(byte_io, 'PNG')"""

from bs4 import BeautifulSoup
import urllib.request
import nltk

#nltk.download()

response = urllib.request.urlopen('http://www.webmindservices.com/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)
#print(freq.items())

"""Logic of Counting words Frequency
for key,val in freq.items():
    print (str(key) + ':' + str(val))"""
    

freq.plot(20, cumulative=False)