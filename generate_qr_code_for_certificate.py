import qrcode
from PIL import Image

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
data = input("Enter the path of the certificate : ")  # Replace with the desired URL or content
qr.add_data(data)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

# Load and resize the logo image
logo_path = "logo.png"  # Replace with the path to your logo image
logo_size = (100, 100)  # Replace with the desired logo size
logo_image = Image.open(logo_path)
logo_image = logo_image.resize(logo_size)

# Calculate the position to place the logo in the center of the QR code
qr_width, qr_height = qr_image.size
logo_width, logo_height = logo_image.size
logo_position = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)

# Paste the logo onto the QR code
qr_image.paste(logo_image, logo_position)

# Save the final QR code with the logo
output_path = "qr_code_with_logo.png"  # Replace with the desired output file path
qr_image.save(output_path)

