# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "https://web.whatsapp.com/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr1.svg", scale=8)

# 2nd method

import pyqrcode
from PIL import Image
from pyqrcode import QRCode

s = "https://web.whatsapp.com/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('myqr2.png', scale=6)