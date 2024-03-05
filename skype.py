#pip install skpy

from skpy import Skype
import os.path #to access file from system

login = Skype("yourmail@gmail.com", "yourpw")

# send image to a person
contact = login.contacts["live:.userid"]
with open("C:/Users/Downloads/skype.png", "rb") as f:
    # rb = binary format
    contact.chat.sendFile(f, "skype.png", image = True)

# create a groupchat
group = login.chats.create(["live: user1id", "live:user2id"])

# Send a msg to one person
contact = login.contacts["live:.userid"]
contact.chat.sendMsg("Hey I am sending u a text through python")

for i in contact:
    print(i)


