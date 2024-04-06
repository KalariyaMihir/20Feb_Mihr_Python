# Practice of qrcode

import qrcode

url = "https://github.com/KalariyaMihir"

qr = qrcode.make(url)

qr.save("mihir.png")