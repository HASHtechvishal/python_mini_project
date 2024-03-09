import qrcode as qr
from PIL import Image
# QRCode able to change qr type

qr = qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,
               box_size=10,border=4,)
qr.add_data("https://www.amazon.in/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("amazon.png")