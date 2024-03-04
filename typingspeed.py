from time import *
import random as r

print(time())
def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
     try:
            if partest[i]!= usertest[i]:
                error = error + 1
     except:
         error = error + 1
         return error
def speed_time(time_s, time_e, userinput):
 time_delay = time_e - time_s
 time_R = round(time_delay, 2)
 speed = len(userinput)/ time_R
 return round(speed)
 
test = ["Hey hope you are learning python", 
        "Welcome to Git"]
test1 = r.choice(test)
print("---Typing speed---")
print(test1)
print()
print()
 #time starts after input is provided
time_1 = time()
#take input from user
testinput=input("Enter: ")
time_2 = time()

print("Speed: ", speed_time(time_1, time_2, testinput),"w/sec")
print("Error: ", mistake(test1, testinput))
