from PIL import Image, ImageOps
import os

def resize_image(image, target_size):
    """
    Resize the image to the target size.

    Args:
        image (PIL.Image): Input image.
        target_size (tuple): Target size (width, height).

    Returns:
        PIL.Image: Resized image.
    """
    return image.resize(target_size, Image.LANCZOS)

def remove_image_background(image):
    """
    Remove the background from the image using Pillow's ImageOps.

    Args:
        image (PIL.Image): Input image.

    Returns:
        PIL.Image: Image with the background removed.
    """
    # Convert image to RGBA mode if it's not already
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Split the image into RGB and alpha channels
    r, g, b, a = image.split()

    # Invert the RGB channels
    r = ImageOps.invert(r)
    g = ImageOps.invert(g)
    b = ImageOps.invert(b)

    # Recombine the RGB channels with the original alpha channel
    return Image.merge("RGBA", (r, g, b, a))

def process_single_image(input_image_path, output_directory, target_size):
    """
    Process a single image: resize, remove background, and save.

    Args:
        input_image_path (str): Path to the input image.
        output_directory (str): Directory to save processed images.
        target_size (tuple): Target size (width, height).
    """
    # Open the input image
    input_image = Image.open(input_image_path)

    # Resize the image to the target size
    resized_image = resize_image(input_image, target_size)

    # Remove background
    processed_image = remove_image_background(resized_image)

    # Save the processed image with the same format and size
    output_path = os.path.join(output_directory, os.path.basename(input_image_path))
    processed_image.save(output_path)
    print(f"Processed image saved at: {output_path}")

def process_images_in_folder(folder_path, output_folder_path, target_size):
    """
    Process all images in a folder: resize, remove background, and save.

    Args:
        folder_path (str): Path to the folder containing images.
        output_folder_path (str): Path to the folder to save processed images.
        target_size (tuple): Target size (width, height).
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    # List all files in the folder
    files = os.listdir(folder_path)

    # Process each image file
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            process_single_image(file_path, output_folder_path, target_size)

def main():
    # Ask the user for the target size
    target_width = int(input("Enter the target width: "))
    target_height = int(input("Enter the target height: "))
    target_size = (target_width, target_height)

    # Ask the user whether to process a single image or a folder
    choice = input("Enter '1' to process a single image or '2' to process images in a folder: ")

    if choice == '1':
        input_image_path = input("Enter the path to the input image: ")
        output_directory = input("Enter the path to the output directory: ")
        process_single_image(input_image_path, output_directory, target_size)
    elif choice == '2':
        folder_path = input("Enter the path to the folder containing images: ")
        output_folder_path = input("Enter the path to the output folder: ")
        process_images_in_folder(folder_path, output_folder_path, target_size)
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
