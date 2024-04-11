from PIL import Image
import os

def generate_mipmap_dimensions(base_size, densities):
    mipmap_dimensions = {}
    for density, scale_factor in densities.items():
        mipmap_dimensions[f"mipmap-{density}"] = (int(base_size * scale_factor), int(base_size * scale_factor))
    return mipmap_dimensions

def resize_and_save_images(input_image_path, output_directory, base_size, densities):
    # Open the input image
    input_image = Image.open(input_image_path)

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Generate mipmap dimensions
    mipmap_dimensions = generate_mipmap_dimensions(base_size, densities)

    # Resize and save images
    for density, dimensions in mipmap_dimensions.items():
        resized_image = input_image.resize(dimensions, Image.LANCZOS)  # Changed line
        output_path = os.path.join(output_directory, f"{density}.png")
        resized_image.save(output_path)
        print(f"Resized image saved at: {output_path}")

input_image_path = "TicTacToe.png"  # Replace with your input image path
output_directory = "resized_images"
base_size = 48
densities = {
    "mdpi": 1,
    "hdpi": 1.5,
    "xhdpi": 2,
    "xxhdpi": 3,
    "xxxhdpi": 4
}

resize_and_save_images(input_image_path, output_directory, base_size, densities)
