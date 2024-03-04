import smtplib as s

obj = s.SMTP("smtp.gmail.com", 587)
obj.ehlo()
obj.starttls()
obj.login("yourmail@gmail.com", "pwww")
subject = "Testing Python"
body= "Hey!! what's up"
message = "subject:{}\n\n{}".format(subject, body)
list=["user1@gmail.com",
      "user2@gmail.com"]
obj.sendmail("yourmail@gmail.com", list, message)
print("Sent mail")
obj.quit()