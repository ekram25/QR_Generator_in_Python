import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://ekram25.github.io/porrtfolio-/" # put your link (web-page) to create QR code for it
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save('text.png')
