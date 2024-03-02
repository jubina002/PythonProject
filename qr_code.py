import qrcode as qr
img = qr.make("https://www.pinterest.com/")

img.save("Pinterest.png")