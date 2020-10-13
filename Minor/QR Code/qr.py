import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# create a qr code of the text given below
qr = pyqrcode.create("Coding With Rajdeep617")
qr.png("my_QRCode.png",scale=8) 
# give the full path where you want to save
# give the name of file

d = decode(Image.open("mycode.png")) # decode the qr code
print(d[0].data.decode("ascii"))