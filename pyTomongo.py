# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:57:08 2019

@author: Anjali Brajendra
"""

import pymongo
import pyttsx3


engine = pyttsx3.init()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["chatbotdb"]
mycol = mydb["client"]

def SaveData(rowid,question,answer):
    mylist = {"_id":rowid,"Question":question, "Answer":answer}
    mycol.insert_one(mylist)
        
def chat():
    flag = True
    while(flag==True):
        user_question = input("Say Somthings: ")
        user_question = user_question.strip();
        if user_question != "q":
            answer = mycol.find_one({"Question":user_question})
            if answer == None:
                print("None")
                engine.say("Not found !! Please tell me its answer so that i can remeber it..")
                engine.setProperty("rate", 160)
                engine.runAndWait()
                print("Not found !! Please tell me its answer so that i can remeber it..")
                user_answer = input();
                user_answer = user_answer.strip()
                #print(mycol.count())
                SaveData(mycol.count() + 1,user_question,user_answer)
                engine.say("Thanks")
                engine.runAndWait()
            else:
                engine.say(answer["Answer"])
                engine.setProperty("rate", 100)
                engine.runAndWait()
                print(answer["Answer"])
        else:
            flag=False
if __name__ == "__main__":
    chat()