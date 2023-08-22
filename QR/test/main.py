import qrcode

data = "https://www.example.com"  # The content you want to encode
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=100,  # Size of each box in pixels
    border=0,  # Size of the border in boxes
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="#200058", back_color=None)  # You can customize colors

img.save("example_qrcode.png")  # Save the QR code image