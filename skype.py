from skpy import Skype as sk
import os.path

s_login = sk("username","password")

contact2 = s_login.contacts["live:.cid.2405frr67567f"]
with open("path of the file","rb") as f:
    contact2.chat.sendFile(f,"file_name",image=True) 


#group = s_login.chats.create(["live:.cid.5645657f78","many more ids"])

#contact = s_login.contacts["live:.cid.2405frr67567f"]
#contact.chat.sendMsg("welcome")

#for i in contact:
    #print(i)