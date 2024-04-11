from PIL import Image

# Load the source image
source_image_path = "TicTacToe.png"
source_image = Image.open(source_image_path)

# Resize the image to 1024x1024 pixels
new_size = (1024, 1024)
enhanced_image = source_image.resize(new_size, Image.LANCZOS)  # LANCZOS is a high-quality resampling filter
enhanced_image.save("enhanced_image.png")

print("Image enhanced to 1024x1024 pixels.")
