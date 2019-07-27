# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:06:41 2018

@author: Anjali Brajendra
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('WebmindBot')

bot.set_trainer(ListTrainer)

#First time for train chatbot with trained data 
for files in os.listdir("E:\Brajendra\Python\Python-Projects\MyChatBot\Project-1\data\english-1/"):
    print(files)
    data = open("E:\Brajendra\Python\Python-Projects\MyChatBot\Project-1\data\english-1/" + files,'r').readlines()
    #bot.storage.drop()
    bot.train(data)

import nltk
import numpy as np
import random
import string # to process standard python strings

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f=open('1.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words



lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    #print(sent_tokens)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    #print(tfidf)
    vals = cosine_similarity(tfidf[-1], tfidf)
    #print(vals)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    #print(flat)
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response






    
while True:
    message = input('You:')
    if message.lower().strip() !='Bye'.lower():
        reply = bot.get_response(message)
        print('ChatBot: ',reply)
    if message.lower().strip()=='Bye'.lower():
        print('ChatBot:','Bye')
        break
    
    
