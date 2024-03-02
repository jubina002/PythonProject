# Conditions
# 1  a-z lower case
# 2  0-9
# 3  . _ @ occurence = 1
# 4  . 2nd or 3rd position

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email: ")
if re.search(email_condition, user_email):
    print("Right email")
else:
    print("Wrong email")
    