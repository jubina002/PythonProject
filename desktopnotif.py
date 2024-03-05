# pip install time
# pip install plyer

from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Take rest",
            message = "Gotta take rest Queen",
            # app_icon="C:/Users/Jubin/OneDrive/Desktop/PP/rest.ico",
            timeout = 10)
        time.sleep(10) #notifies u every 10 sec

# To stop the Process:
# go to task manager
# go to Process
# python file -> end task
        
# pythonw file.py
# to run your python in the background
    