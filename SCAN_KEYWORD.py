import time
import robomaster
from robomaster import conn
from MyQR import myqr
from PIL import Image


QRCODE_NAME = "qrcode.png"

helper = conn.ConnectionHelper()
info = helper.build_qrcode_string(ssid="hqy1433", password="clm1314520")
myqr.run(words=info)
time.sleep(1)
img = Image.open(QRCODE_NAME)
img.show()
if helper.wait_for_connection():
    print("Connected!")
else:
    print("Connect failed!")
