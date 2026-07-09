import qrcode

# Take input from the user
data = input("Enter text or URL: ")

# Create QR Code
qr = qrcode.make(data)

# Save the QR Code
filename = "output_qr.png"
qr.save(filename)

print("QR Code generated successfully!")
print("Saved as:", filename)

# Show the QR Code
qr.show()

# run this in terminal pip install qrcode[pil]
#Enter tert or URL type -> https://google.com
# now we'll receive the QR code, scan it and it is going to take us to google
#output would be OR code generated successfully