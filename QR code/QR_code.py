import qrcode as qr

# function in qrcode make()

img = qr.make("https://www.youtube.com/@wrestleshorts")
img.save("wwe_youtube.png") # name of the file

