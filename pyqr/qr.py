

import qrcode

url = input('enter the url here: ')
img = qrcode.make(url)
img.save('qr.png')
