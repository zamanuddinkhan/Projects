import qrcode

# Get URL from user
url = input("Enter The URL: ").strip()

# File path to save the QR code
file_path = "C:\\Users\\Zamanuddin Khan\\Downloads\\Coding Area\\Projects\\QR-Code-Generator\\qrcode.png"

# Create QR Code object
qr = qrcode.QRCode()

# Add URL data
qr.add_data(url)

# Generate QR Code image
img = qr.make_image()

# Save image
img.save(file_path)

print(f"QR Code saved successfully at:\n{file_path}")