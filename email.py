# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:42:43 2018

@author: Anjali Brajendra
"""
import os
import imaplib
import email

username = "brajendrashukla25@gmail.com"
password ="shukl@1985"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,password)
print(mail.list())
mail.select("Airtel")


def getAttachement(msg):
    for attach in msg.walk():
        '''if attach.get_content_maintype=='multipart':
            continue
        if attach.get('Content-Dispostion') is None:
            continue
        '''
        fileName = attach.get_filename()
        if bool(fileName):
            file_path = os.path.join('Attachement\\',fileName)
            print(file_path)
            with open(file_path,'wb') as f:
                f.write(attach.get_payload())
            
mtype,data = mail.search(None,'ALL')
mail_Ids = data[0]

ids = mail_Ids.split();
ids = ids[:1]
#print(ids)
file_index = 1;
for x in ids:
    try:
        stat,m_data = mail.fetch(x,'(RFC822)')
        mail_data = email.message_from_bytes(m_data[0][1])
        #file = open("Mails\\" + str(mail_data["Subject"]) + ".txt", "wb") 
        #file.write(str(mail_data.get_payload(0)))
        getAttachement(mail_data)
        print("--------------------------------")
    except:
         print("Something went wrong when writing to the file")
         file = open("Mails\\" + str(file_index) + ".txt", "w") 
         file.write(str(mail_data))
         file_index = file_index  + 1;
       
    finally:
        file.close() 

mail.logout()

