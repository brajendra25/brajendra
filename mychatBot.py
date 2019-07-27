# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:17:25 2019

@author: Anjali Brajendra
"""

import pyttsx3
import pyTomongo as mong
engine = pyttsx3.init()
'''
file = open("1.txt",'r')
fileTxt = file.readlines()
file.close();
isQuestion = True;
questionList = [];
answerList=[];
for line in fileTxt:
    if(isQuestion):
        questionList.append(line.lower().replace('\n',''))
        isQuestion = False
    else:
        answerList.append(line.lower().replace('\n',''))
        isQuestion = True
'''

flag=True
i = 0;
while(flag==True):
    file = open("1.txt",'r')
    fileTxt = file.readlines()
    #print(fileTxt)
    file.close();
    isQuestion = True;
    questionList = [];
    answerList=[];
    for line in fileTxt:
        if(isQuestion):
            questionList.append(line.strip().lower().replace('\n',''))
            isQuestion = False
        else:
            answerList.append(line.strip().lower().replace('\n',''))
            isQuestion = True
    #print("Question: ",questionList)      
    text = input("Say Somthings: ")
    text = text.strip();
    if text != "q":
        if text in questionList:
            if engine.isBusy() ==  True:
                index = questionList.index(text)
                #print(index)
                i = i + 1;
                ans = answerList[index]
                #print(ans)
                engine.say(ans)
                engine.setProperty("rate", 100)
                engine.runAndWait()
                print(ans)
                mong.SaveData(i,text,ans)
        else:
            engine.say("Not found !! Please tell me its answer so that i can remeber it..")
            engine.setProperty("rate", 160)
            engine.runAndWait()
            print("Not found !! Please tell me its answer so that i can remeber it..")
            user_answer = input();
            user_answer = user_answer.strip()
            if user_answer!="bye":
                user_file = open("1.txt","a")
                 #print(fileTxt)
                user_file.write(text + '\n')
                user_file.write(user_answer + '\n')
                user_file.close()
                if user_answer == "bye":
                    flag=False
    else:
        flag=False
    