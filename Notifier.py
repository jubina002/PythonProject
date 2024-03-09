import datetime
import time
from plyer import notification
import yfinance as yf 
msft = yf.Ticker("MSFT")
data = msft.info


while True:
    notification.notify(
    title = "MSFT data".format(datetime.date.today()),
    message = "Current Price = {cp} \nDay Low = {dl} \nDay High ={dh}".format(
        cp = data["currentPrice"],
        dl = data["regularMarketDayLow"],
        dh = data["regularMarketDayHigh"]
    ),
    app_icon = "C:/Users/Jubin/OneDrive/Desktop/PP/bell.ico",
    timeout = 10
    )
    time.sleep(60*60*2)