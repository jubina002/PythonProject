import smtplib as s

obj = s.SMTP("smtp.gmail.com", 587)
obj.ehlo()
#EHLO ("Extended Hello") is the SMTP command the client uses to tell the server that it is an SMTP client
obj.starttls()
# STARTTLS is a protocol command that tells the email server that the other party (email server or client)
# wants to switch from an insecure plain text connection to a secure connection using TLS or SSL
obj.login("yourmail@gmail.com", "pwww")
subject = "Testing Python"
body= "Hey!! what's up"
message = "subject:{}\n\n{}".format(subject, body)
list=["user1@gmail.com",
      "user2@gmail.com"]
obj.sendmail("yourmail@gmail.com", list, message)
print("Sent mail")
obj.quit()
