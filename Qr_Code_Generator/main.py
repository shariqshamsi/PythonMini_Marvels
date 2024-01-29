import qrcode as qr
img = qr.make("https://www.facebook.com/btechdigital")
img.save("B-Tech.png")